#!/bin/env python

# Module to help convert OpenSceneGraph C++ examples to python

import re
import textwrap
from collections import OrderedDict

import clang.cindex
from clang.cindex import CursorKind, TokenKind


INDENT_SIZE = 4
CURRENT_INDENT = 0

# Conversion from C++ to python
punctuation_translator = {
    '->': '.',
    ':': '',
    '::': '.',
    '{': '',
    '}': '',
    ',': ', ',
    '&': '',
    '&&': ' and ',
    '||': ' or ',
    ';': '\n',
    '=': ' = ',
    '==': ' == ',
    '!': ' not ',
    '<<': ' << ',
}

keyword_translator = {
    'break': 'break',
    'catch': 'except',
    'class': 'class',
    'continue': 'continue',
    'double': 'float',
    'else': 'else',
    'for': 'for',
    'false': 'False',
    'delete': 'del',
    'if': 'if',
    'long': 'int',
    'new': '',
    'nullptr': 'None',
    'private': '',
    'protected': '',
    'public': '',
    'return': 'return ',
    'short': 'int',
    'struct': 'class',
    'this': 'self',
    'throw': 'raise',
    'true': 'True',
    'try': 'try',
    'while': 'while',
}

# Conversion from C++ to python
method_translator = {
    'operator()': '__call__',
}


class LocationComparable():
    "Helper class to compare file locations of clang tokens and cursors"
    def __init__(self, nibble=None, line=None, column=None):
        if nibble is not None:
            self.line = int(nibble.location.line)
            self.col = int(nibble.location.column)
        else:
            self.line = line
            self.col = column
        
    def __eq__(self, rhs):
        return not self != rhs
    
    def __ne__(self, rhs):
        if self.line != rhs.line:
            return True
        elif self.col != rhs.col:
            return True
        else:
            return False
        
    def __lt__(self, rhs):
        if self.line < rhs.line:
            return True
        elif self.line > rhs.line:
            return False
        elif self.col < rhs.col:
            return True
        else:
            return False
        
    def __gt__(self, rhs):
        if self.line > rhs.line:
            return True
        elif self.line < rhs.line:
            return False
        elif self.col > rhs.col:
            return True
        else:
            return False
        
    def __le__(self, rhs):
        return not self > rhs
    
    def __ge__(self, rhs):
        return not self < rhs


class CursorNibble(LocationComparable):
    """
    CursorNibble represents one node of a clang abstract syntax tree.
    Nibble represents a union of cursors and tokens
    """
    def __init__(self, cursor, file_filter=None):
        LocationComparable.__init__(self, cursor)
        self.cursor = cursor
        self.file_filter = file_filter
        # use property for cached location
        self.line = int(self.location.line)
        self.col = int(self.location.column)
    
    def get_child_cursors(self):
        for child in self.cursor.get_children():
            if self.file_filter is not None and str(child.location.file) != self.file_filter:
                continue
            yield CursorNibble(child)
    
    def get_child_nibbles(self):
        """
        generate an ordered sequence of child nodes, interspersed with orphaned
        tokens that belong to no child node
        """
        tg = self.get_child_tokens()
        cg = self.get_child_cursors()
        t = next(tg, None)
        c = next(cg, None)
        while t is not None or c is not None:
            if c is None:
                yield t
                t = next(tg, None)
            elif t is None:
                yield c
                c = next(cg, None)
            elif t < c: # orphan token
                yield t # orphan
                t = next(tg, None)
            elif t <= c.end: # token internal to child cursor
                t = next(tg, None) # consume without emitting
            else: # child cursor after internal tokens exhausted
                yield c
                c = next(cg, None)
            # Discard tokens that are past the end of our stated range
            if t is not None and t > self.end:
                t = None
        
    def get_child_tokens(self):
        for token in sorted(list(self.cursor.get_tokens()), key=comparable_location):
            if self.file_filter is not None and str(token.location.file) != self.file_filter:
                continue
            yield TokenNibble(token)
        
    def get_namespaces(self):
        "enumerate all namespaces, such as 'osg::', used in this file, to help enumerate python imports"
        ns = set()
        if self.kind == CursorKind.NAMESPACE_REF:
            yield self.cursor
        # for child in self.get_child_cursors():
        #     for ns in child.get_namespaces():
        #         yield ns
        previous_token = None
        for nibble in self.get_child_nibbles():
            if isinstance(nibble, CursorNibble):
                previous_token = None
                for ns in nibble.get_namespaces():
                    yield ns
            else: # must be a token
                if nibble.kind == TokenKind.PUNCTUATION and nibble.spelling == '::':
                    if previous_token is None:
                        continue
                    if previous_token.kind != TokenKind.IDENTIFIER:
                        continue
                    yield previous_token
                previous_token = nibble
    
    def get_all_strings(self, debug=False):
        for nibble in self.get_child_nibbles():
            for py_string in nibble.get_py_strings(debug=debug):
                yield py_string
    
    def get_py_strings(self, debug=False):
        if debug:
            yield str(self.kind)
            yield str(self.location.line)
            yield "."
            yield str(self.location.column)
            yield '-'
            yield str(self.end.line)
            yield "."
            yield str(self.end.col)
            yield "["
        if self.kind in rules:
            for item in rules[self.kind]:
                # Could be a string...
                if isinstance(item, basestring):
                    yield item
                else: # ...or a string generator
                    for string in item(self, debug=debug):
                        yield string
        else:
            for py_string in self.get_all_strings(debug=debug):
                    yield py_string
        if debug:
            yield "]"
                    
    def get_real_beginning(self):
        # Use location of first child, including early tokens
        return self.get_child_nibbles().next().location
                
    end = property(lambda self: LocationComparable(
                line=self.cursor.extent.end.line,
                column=self.cursor.extent.end.column))
    kind = property(lambda self: self.cursor.kind)
    location = property(lambda self: self.get_real_beginning())
    spelling = property(lambda self: self.cursor.spelling)


# Nibble is union of tokens and cursors
class TokenNibble(LocationComparable):
    "A Token is a small chunk of C++ source code text, lexically parsed by clang"
    def __init__(self, token):
        LocationComparable.__init__(self, token)
        self.token = token
        
    def get_child_cursors(self):
        return # nothing
    
    def get_child_nibbles(self):
        return # nothing
    
    def get_child_tokens(self):
        return # nothing
        
    def get_py_strings(self, debug=False):
        if debug:
            yield str(self.kind)
            yield str(self.location.line)
            yield "."
            yield str(self.location.column)
        if self.kind in rules:
            for item in rules[self.kind]:
                # Could be a string...
                if isinstance(item, basestring):
                    yield item
                else: # ...or a string generator
                    for string in item(self):
                        yield string
        else:
            yield self.spelling
    
    kind = property(lambda self: self.token.kind)
    location = property(lambda self: self.token.location)
    spelling = property(lambda self: self.token.spelling)


class TranslatedPyProgram():
    """
    TranslatedProgram is the main class for translating OpenSceneGraph C++ example program in to python.
    One TranslatedProgram can be composed of multiple source files.
    """
    def __init__(self, src_files, args, indent=4):
        self.tus = []
        for s in src_files:
            self.tus.append(TranslationUnit(src_file=s, args=args))
            
    def get_py_strings(self):
        # Top header
        yield textwrap.dedent("""\
        #!/bin/env python
        
        # This is an OpenSceneGraph example program, automatically translated from C++ into python
        
        import sys
        
        """)
        # osg import statements
        osg_imports = set()
        for tu in self.tus:
            for namespace in tu.get_namespaces():
                ns = str(namespace.spelling)
                if ns.startswith("osg"):
                    osg_imports.add(ns)
        if len(osg_imports) > 0:
            for imp in sorted(osg_imports):
                yield "from osgpypp import %s\n" % imp
            yield "\n" # blank line after third party imports
        # Main program text
        for tu in self.tus:
            for s in tu.get_py_strings():
                yield s
        # Bottom footer
        yield textwrap.dedent("""\
        
        
        if __name__ == '__main__':
            ret_val = main(len(sys.argv), sys.argv)
            if ret_val is not None:
                sys.exit(ret_val)
        
        """)


class TranslationUnit(CursorNibble):
    "TranslationUnit represents one C++ source file to be translated"
    def __init__(self, src_file, args=[]):
        index = clang.cindex.Index.create()
        self.tu = index.parse(src_file, args=args)
        self.main_file = str(self.tu.spelling)
        CursorNibble.__init__(self, self.tu.cursor, file_filter=self.main_file)

    def get_py_strings(self):
        # TODO - translation unit header
        for string in CursorNibble.get_py_strings(self):
            yield string
            if string.endswith('\n'):
                yield ' '*CURRENT_INDENT


def call_expression(cursor, debug=False):
    prefix = []
    contents = []
    for nibble in cursor.get_child_nibbles():
        if nibble.spelling == cursor.spelling:
            if isinstance(nibble, CursorNibble):
                prefix.append(nibble)
        else:
            contents.append(nibble)
    p = ""
    if len(prefix) > 0:
        p = prefix[0].spelling
    if p == "operator->":
        yield "self."
    elif p == "operator!":
        # yield "not "
        pass
    else:
            for c in prefix:
                for py_string in c.get_py_strings(debug):
                    yield py_string
    if len(contents) < 1:
        pass
    # Skip initial part of variable declaration with "new"
    elif contents[-1].kind == TokenKind.PUNCTUATION and contents[-1].spelling == "=":
        pass
    else:
        for c in contents:
            for py_string in c.get_py_strings(debug):
                yield py_string


def class_bases(class_cursor, debug=False):
    bases = []
    for c in class_cursor.get_child_cursors():
        if c.kind == CursorKind.CXX_BASE_SPECIFIER:
            bases.append(c)
    for b in bases:
        for py_string in b.get_py_strings():
            yield py_string
        if b is not bases[-1]:
            yield ", "


def class_constructors(cls, debug=False):
    ctors = []
    bases = []
    fields = OrderedDict()
    for child in cls.get_child_cursors():
        if child.kind == CursorKind.CXX_BASE_SPECIFIER:
            bases.append(child)
        elif child.kind == CursorKind.CONSTRUCTOR:
            ctors.append(child)
        elif child.kind == CursorKind.FIELD_DECL:
            ident = field_identifier(child, debug).next()
            fields[ident] = child
    for ctor in ctors:
        for py_string in cursor_constructor(
                    ctor, 
                    class_name = cls.spelling, 
                    fields=fields, 
                    bases=bases,
                    debug=debug):
            yield py_string
    # TODO: default constructor for constructor-less class


def class_contents(cursor, debug=False):
    found_a_cursor = False
    for nibble in cursor.get_child_nibbles():
        if isinstance(nibble, CursorNibble):
            found_a_cursor = True
        if isinstance(nibble, TokenNibble) and not found_a_cursor:
            continue # already handled
        if nibble.kind == CursorKind.CXX_BASE_SPECIFIER:
            continue # already handled
        if nibble.kind == CursorKind.CONSTRUCTOR:
            continue # already handled
        elif nibble.kind == CursorKind.FIELD_DECL:
            continue
        for py_string in nibble.get_py_strings():
            yield py_string
    

def comparable_location(nibble):
    return LocationComparable(nibble)


def ctor_base_args(ctor, bases={}, debug=False):
    # Clang parses base constructor arguments only as a series of tokens
    # So crudely parse those tokens
    # Bar(carg1, carg2) : public Base(barg1, barg2), foo(3), baz("Hey!") {schwing();}
    # this method should generate the "barg1, barg2", if any
    # use a state machine
    state = "pre-colon"
    paren_level = 0
    for nibble in ctor.get_child_nibbles():
        if state == "pre-colon":
            if nibble.kind == TokenKind.PUNCTUATION and nibble.spelling == ":":
                state = "pre-paren"
        elif state == "pre-paren":
            if nibble.kind == TokenKind.PUNCTUATION and nibble.spelling == "(":
                state = "base-args"
                paren_level = 1
            elif nibble.kind == TokenKind.PUNCTUATION and nibble.spelling == ",":
                break # no arguments to parse
            elif isinstance(nibble, CursorNibble):
                break # no arguments to parse
        elif state == "base-args":
            if nibble.kind == TokenKind.PUNCTUATION and nibble.spelling == "(":
                paren_level += 1
            elif nibble.kind == TokenKind.PUNCTUATION and nibble.spelling == ")":
                paren_level -= 1
            if paren_level < 1:
                break # Done with argument parsing
            for py_string in nibble.get_py_strings():
                yield py_string
    

def ctor_nodes(cursor, debug=False):
    "Avoid child nodes that cause trouble for constructor"
    for child in cursor.get_children():
        if child.kind == CursorKind.MEMBER_REF:
            continue
        if child.kind == CursorKind.CALL_EXPR:
            continue
        yield child


def cursor_all_strings(cursor, debug=False):
    for py_string in cursor.get_all_strings():
        yield py_string


def cursor_compound_child(cursor, debug=False):
    for child in cursor.get_child_nibbles():
        if child.kind == CursorKind.COMPOUND_STMT:
            for py_string in child.get_py_strings(debug=debug):
                yield py_string
            return


def cursor_constructor(ctor, class_name, fields=None, bases=None, debug=False):
    yield '\n'
    yield "def __init__(self"
    for arg in ctor.get_child_cursors():
        if not arg.kind == CursorKind.PARM_DECL:
            continue
        yield ", "
        yield arg.spelling
        # TODO: default parameter values
    yield "):"
    inc_indent()
    yield "\n"
    # Base initalizer
    yield 'super('
    yield class_name
    yield', self).__init__('
    # TODO: use correct base initializer arguments
    for py_string in ctor_base_args(ctor, bases=bases):
        yield py_string
    yield ')'
    yield '\n'
    # Emit one line of code for each member field initializer
    # First visit all explicit field initializers in this constructor,
    # and store the initialization value
    init_args = dict()
    for child in ctor.get_child_cursors():
        if child.kind != CursorKind.CALL_EXPR:
            continue
        init = list(child.get_child_nibbles())
        ident = str(init[0].spelling)
        if ident in fields:
            field = fields[ident]
            val = init[2] # trim initial id and open paren
            strings = list(val.get_py_strings())
            args = strings[:-1] # trim final close paren
            init_args[ident] = args
    # Emit field initializers one by one
    for ident, field in fields.iteritems():
        yield "self."
        yield ident         
        yield " = "
        # Field constructors
        # A) Explicit field initializer...
        if ident in init_args:
            for py_string in init_args[ident]:
                yield py_string
        else: # ...or B) Default constructor using field type
            for py_string in field_type(field):
                yield py_string
                yield '('
                yield ')'
        yield '\n'
    # Emit remainder of constructor code
    for py_string in cursor_compound_child(ctor, debug):
        yield py_string
    dec_indent()
    
    
def cursor_first_tokens(cursor):
    for child in cursor.get_child_nibbles():
        if isinstance(child, TokenNibble):
            yield child
        else:
            break
        

def debug_nibble(self, debug=True):
    yield str(self.kind)
    yield str(self.location.line)
    yield "."
    yield str(self.location.column)
    yield '-'
    yield str(self.end.line)
    yield "."
    yield str(self.end.col)
    yield "["
    for py_string in self.get_all_strings(debug=True):
            yield py_string
    yield "]"


def dec_indent(cursor=None, debug=False):
    global CURRENT_INDENT
    CURRENT_INDENT -= INDENT_SIZE
    if CURRENT_INDENT < 0:
        raise Exception("Hey! indent should not be negative, but is")
    return ''


def displayname(cursor, debug=False):
    yield cursor.displayname
    

def field_identifier(field, debug=False):
    for child in field.get_child_nibbles():
        if child.kind == TokenKind.IDENTIFIER:
            for py_string in child.get_py_strings(debug):
                yield py_string


def field_type(field, debug=False):
    for child in field.get_child_nibbles():
        if child.kind == TokenKind.IDENTIFIER:
            continue
        if child.kind == TokenKind.PUNCTUATION and child.spelling == ";":
            continue
        for py_string in child.get_py_strings(debug):
            yield py_string


def if_conditional(cursor, debug=False):
    for child in cursor.get_child_cursors():
        py_strings = list(child.get_py_strings());
        # Trim off final ")"
        for py_string in py_strings[:-1]:
                yield py_string
        break # First cursor only
    
def if_consequence(cursor, debug=False):
    found_first = False
    for child in cursor.get_child_nibbles():
        if not found_first:
            if isinstance(child, CursorNibble):
                found_first = True
            continue # skip first cursor, and all before it
        else:   
            for py_string in child.get_py_strings(debug):
                yield py_string
    

def inc_indent(cursor=None, debug=False):
    global CURRENT_INDENT
    CURRENT_INDENT += INDENT_SIZE
    return ''
        

def kind(cursor, debug=False):
    return str(cursor.kind)


def location(nibble, debug=False):
    return nibble.location


def method_name(method, debug=False):
    if method.spelling in method_translator:
        yield method_translator[method.spelling]
    else:
        yield method.spelling


def params(cursor, debug=False):
    first_arg = True
    for arg in cursor.get_child_cursors():
        if not arg.kind == CursorKind.PARM_DECL:
            continue
        if not first_arg:
            yield ", "
        yield arg.spelling
        first_arg = False
        # TODO: default parameter values


def params_with_self(cursor, debug=False):
    yield "self"
    for arg in cursor.get_child_cursors():
        if not arg.kind == CursorKind.PARM_DECL:
            continue
        yield ", "
        yield arg.spelling
        # TODO: default parameter values


def spelling(cursor, debug=False):
    return cursor.spelling    


def token_precedes(token, line1, col1):
    if token is None:
        return False
    if token.location.line < line1:
        return True
    elif token.location.line == line1 and token.location.column < col1:
        return True
    else:
        return False


def token_comment(token, indent=0, debug=False):
    c = str(token.spelling)
    if c.startswith('/*'):
        c = re.sub(r'^/\*', '#', c)
        for line in c.split('\n'):
            yield '#'
            yield line
            yield '\n'
    elif c.startswith("//"):
        c = re.sub(r"^//", "#", c)
        yield c
        yield '\n'
    else:
        raise "Unexpected comment %s" % token.spelling


def token_keyword(token, debug=False):
    if token.spelling in keyword_translator:
        yield keyword_translator[token.spelling]
    else:
        yield token.spelling
        yield ' '


def token_punctuation(token, indent=0, debug=False):
    if token.spelling in punctuation_translator:
        yield punctuation_translator[token.spelling]
    else:
        yield token.spelling
        
        
def decl_stmt(cursor, debug=False):
    """
    # Four types of variable declarations:
    A) type foo; // ==> foo = type()
    B) type foo(args); // ==> foo = type(args)
    C) type foo = <whatever>; // ==> foo = <whatever>
    D) type1 foo = new type2; // ==> foo = type2()
    """
    # Is there an equals sign?
    found_equals = False
    var_decl = None
    after_equals = []
    equals_token = None
    for token in cursor.get_child_tokens(): # Look in ALL tokens for equals sign
        if token.kind == TokenKind.PUNCTUATION and token.spelling == "=":
            found_equals = True # Case C
            equals_token = token
    # 
    type_nibbles = []
    for nibble in cursor.get_child_nibbles():
        if var_decl is None:
            if nibble.kind == CursorKind.VAR_DECL:
                var_decl = nibble
            else:
                type_nibbles.append(nibble)
        elif found_equals and nibble > equals_token:
            after_equals.append(nibble)
    yield var_decl.spelling
    yield ' = '
    # Case C
    if len(after_equals) > 0:
        # yield "Case 'C': "
        for nibble in after_equals:
            for py_string in nibble.get_py_strings():
                yield py_string
    elif found_equals:
        final_nibble = list(var_decl.get_child_nibbles())[-1]
        for py_string in final_nibble.get_py_strings():
            yield py_string
    else:
        found_call = False
        for nibble in var_decl.get_child_cursors():
            if nibble.kind == CursorKind.CALL_EXPR:
                found_call = True
                # Print contents without identifier
                # yield "Case 'B': "
                yield '('
                for subnibble in nibble.get_child_cursors():
                    if subnibble.kind == TokenKind.IDENTIFIER: # Don't repeat variable name
                        continue
                    else:
                        for py_string in subnibble.get_py_strings():
                            yield py_string
            else:
                for py_string in nibble.get_py_strings():
                    yield py_string
        if not found_call:
            # yield "Case 'A': "
            yield '()' # case A

            
rules = {
        CursorKind.CALL_EXPR: [call_expression],
        CursorKind.CLASS_DECL: [
            '\n\n\n', 
            'class', ' ', spelling, '(',
            class_bases,
            ')', ':', 
            inc_indent,
            '\n',
            class_constructors,
            class_contents,
            dec_indent,],
    CursorKind.CXX_METHOD: ['\n\n', "def ", method_name, "(", params_with_self, "):", 
            inc_indent, "\n", cursor_compound_child, dec_indent,],
    CursorKind.DECL_STMT: [decl_stmt, '\n', 
                           # debug_nibble, 
                           ],
    CursorKind.FUNCTION_DECL: ['\n\n', "def ", spelling, "(", params, ")", ":", 
            inc_indent, "\n", cursor_compound_child, dec_indent,],
    CursorKind.IF_STMT: ["if ", if_conditional, ":", inc_indent, "\n", if_consequence, dec_indent, '\n'],
    # CursorKind.VAR_DECL: [],
    TokenKind.COMMENT: [token_comment],
    TokenKind.KEYWORD: [token_keyword],
    TokenKind.PUNCTUATION: [token_punctuation],
    }


def main():
    osg_src_dir = "F:/Users/cmbruns/build/OpenSceneGraph-3.2.1/OpenSceneGraph-3.2.1/"
    # osg_src_dir = "C:/Users/cmbruns/git/osg/"
    examples_src = osg_src_dir + "examples/"
    osg_includes = osg_src_dir + "include/"
    src_file = examples_src + "/osggraphicscost/osggraphicscost.cpp"

    args = ["-I%s"%osg_includes, '-x', 'c++', '-D__CODE_GENERATOR__']
    translated_program = TranslatedPyProgram([src_file,], args=args)
    py_prog = ""
    for s in translated_program.get_py_strings():
        py_prog += s
    print py_prog


if __name__ == "__main__":
    main()
