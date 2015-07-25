#!/bin/env python

# Module to help convert OpenSceneGraph C++ examples to python

import re
import textwrap

import clang.cindex
from clang.cindex import CursorKind, TokenKind


INDENT_SIZE = 4

# Conversion from C++ to python
punctuation_translator = {
    '->': '.',
    ':': '',
    '::': '.',
    '{': '\n',
    '}': '\n',
    ',': ', ',
    '&': '',
    '&&': ' and ',
    '||': ' or ',
    ';': '\n',
    '=': ' = ',
    '==': ' == ',
    '!': ' not ',
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
    'return': 'return',
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
            elif t <= c: # token internal to child cursor
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
    
    def get_all_strings(self):
        for nibble in self.get_child_nibbles():
            for py_string in nibble.get_py_strings():
                yield py_string
    
    def get_py_strings(self):
        """
        yield str(self.kind)
        yield str(self.location.line)
        yield "."
        yield str(self.location.column)
        """
        if self.kind in rules:
            for item in rules[self.kind]:
                # Could be a string...
                if isinstance(item, basestring):
                    yield item
                else: # ...or a string generator
                    for string in item(self):
                        yield string
        else:
            for py_string in self.get_all_strings():
                    yield py_string
                    
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
        
    def get_py_strings(self):
        """
        yield str(self.kind)
        yield str(self.location.line)
        yield "."
        yield str(self.location.column)
        """
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
            self.tus.append(TranslationUnit(src_file=s, args=args, indent=indent))
            
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
            main(sys.argv)
        
        """)


class TranslationUnit(CursorNibble):
    "TranslationUnit represents one C++ source file to be translated"
    def __init__(self, src_file, args=[], indent=4):
        index = clang.cindex.Index.create()
        self.tu = index.parse(src_file, args=args)
        self.main_file = str(self.tu.spelling)
        CursorNibble.__init__(self, self.tu.cursor, file_filter=self.main_file)
        self.current_indent = 0

    def dec_indent(self):
        self.current_indent -= indent
        if self.current_indent < 0:
            raise Exception("negative indent")        
    def get_py_strings(self):
        # TODO - translation unit header
        for string in CursorNibble.get_py_strings(self):
            yield string
            if string.endswith('\n'):
                yield ' '*self.current_indent

    def inc_indent(self):
        self.current_indent += 4


def py_type(cursor):
    "Convert C++ type reference to python type name"
    t = ""
    # Limit token parsing to tokens that fall within the specified cursor bounds
    end_pos = [cursor.extent.end.line, cursor.extent.end.column]
    for token in cursor.get_tokens():
        if token.location.line > end_pos[0]:
            break
        if token.location.line == end_pos[0] and token.location.column > end_pos[1]:
            break
        if token.kind == TokenKind.KEYWORD:
            continue # no keywords, like "public"
        elif token.kind == TokenKind.IDENTIFIER:
            t += token.spelling
        elif token.spelling in punctuation_translator and token.kind == TokenKind.PUNCTUATION:
            t += punctuation_translator[token.spelling]
        else:
            t += token.spelling # TODO??
            t += "#"
            t += str(token.kind)
            # print token.kind, token.spelling # TODO
    yield t


def all_nodes(cursor):
    for child in cursor.get_children():
        yield child

def all_tokens(cursor):
    result = ""
    s = cursor.extent.start
    e = cursor.extent.end
    for t in cursor.get_tokens():
        if t.location.line < s.line:
            continue
        if t.location.line > e.line:
            continue
        if t.location.line == s.line and t.location.column < s.column:
            continue
        if t.location.line == e.line and t.location.column > e.column:
            continue
        result += t.spelling
    return [result,]

def arg_nonmatching(cursor):
    match = None
    for match in matching_child(cursor):
        break
    args = []
    for c in cursor.get_children():
        if match is not None and  c == match:
            continue
        args.append(c)
    return [", ".join([string_for_cursor(c) for c in args]),]

def args(cursor):
    a = []
    if (cursor.kind == CursorKind.CONSTRUCTOR or (cursor.kind == 
                    CursorKind.CXX_METHOD and not cursor.is_static_method())):
        a.append("self")
    for child in cursor.get_children():
        if not child.kind == CursorKind.PARM_DECL:
            continue
        a.append(child.spelling)
    return "(" + ", ".join(a) + ")"

def call_expression(cursor):
    prefix = list(matching_child(cursor))
    p = ""
    if len(prefix) > 0 and str(prefix[0]) != "":
        p = prefix[0].spelling
    if p == "operator->":
        yield "self"
        for c in arg_nonmatching(cursor):
            yield c
    elif p == "operator!":
        yield "not "
        for c in arg_nonmatching(cursor):
            yield c
    else:
        for c in prefix:
            yield c
        yield "("
        for c in arg_nonmatching(cursor):
            yield c
        yield ")"

def class_bases(class_cursor):
    bases = []
    for c in class_cursor.get_child_cursors():
        if c.kind == CursorKind.CXX_BASE_SPECIFIER:
            bases.append(c)
    for b in bases:
        for py_string in b.get_py_strings():
            yield py_string
        if b is not bases[-1]:
            yield ", "


def comparable_location(nibble):
    return LocationComparable(nibble)


def compound_statement(cursor):
    for child in cursor.get_children():
        yield indent(cursor)
        yield child
        yield "\n"
    
def ctor_init(cursor):
    "parse out initializers, if any, from constructor"
    # Don't look after first child item
    first_pos = [cursor.extent.start.line, cursor.extent.start.column]
    last_pos = [cursor.extent.end.line, cursor.extent.end.column]
    parsed_members = list()
    for c in cursor.get_children():
        if c.kind == CursorKind.PARM_DECL: # go past constructor arguments
            first_pos = [c.extent.end.line, c.extent.end.column+1]
            continue
        if c.kind == CursorKind.MEMBER_REF: # but take note of member initializers
            parsed_members.append(c)
            continue
        if c.kind == CursorKind.CALL_EXPR: # and the second part of the initializer
            continue
        # First generic child found, probably COMPOUND_STMT. Stop searching before this point
        last_pos = [c.location.line, c.location.column - 1]
        break
    found_colon = False
    paren_level = 0
    initializers = []
    for t in cursor.get_tokens():
        if t.location.line < first_pos[0]:
            continue
        if t.location.line > last_pos[0]:
            break
        if t.location.line == first_pos[0] and t.location.column < first_pos[1]:
            continue
        if t.location.line == last_pos[0] and t.location.column > last_pos[1]:
            break
        if not found_colon and t.kind == TokenKind.PUNCTUATION and t.spelling == ":":
            found_colon = True
            initializers.append([])
            continue
        if not found_colon:
            continue
        # inside parentheses, anything can happen, without advancing to the next initializer
        if t.kind == TokenKind.PUNCTUATION and t.spelling == "(":
            paren_level += 1
        if t.kind == TokenKind.PUNCTUATION and t.spelling == ")":
            paren_level -= 1
        # Commas signal separate initializers
        if paren_level == 0 and t.kind == TokenKind.PUNCTUATION and t.spelling == ",":
            initializers.append([])
            continue
        # If we get this far, the current token belongs in the current intializier
        initializers[-1].append(t)
    result = ""
    # Emit one initializer per line
    for i in initializers:
        if len(i) < 1:
            continue
        result += indent(cursor)
        # Separate stuff before parentheses from after parentheses
        if i[-1].spelling != ")":
            print i[-1].kind, i[-1].spelling
            raise Exception("Hey!, I expected a parenthesis there!")
        # find first parenthesis
        pre_paren = []
        in_paren = []
        found_paren = False
        for tok in i[:-1]:
            if not found_paren and tok.spelling == "(":
                found_paren = True
                continue
            if found_paren:
                in_paren.append(tok)
            else:
                pre_paren.append(tok)
        field = translate_tokens(pre_paren)
        value = translate_tokens(in_paren)
        # Is it a field or a base initializer?
        if (field in [c.spelling for c in parsed_members]):
            # Field initializer
            result += "self."+field+" = "+value
        else:
            # Assume base class initializer
            result += field+".__init__(self, "+value+")"
        result += "\n"
    return result

def ctor_nodes(cursor):
    "Avoid child nodes that cause trouble for constructor"
    for child in cursor.get_children():
        if child.kind == CursorKind.MEMBER_REF:
            continue
        if child.kind == CursorKind.CALL_EXPR:
            continue
        yield child

def cursor_all_strings(cursor):
    for py_string in cursor.get_all_strings():
        yield py_string

def debug(cursor):
    yield str(cursor.kind)

def dec_indent(cursor):
    global indent_level
    indent_level -= INDENT_SIZE
    return []

def displayname(cursor):
    yield cursor.displayname
    
main_file = None
indent_level = 0
def filter_by_file(cursor):
    for child in cursor.get_children():
        if str(child.location.file) != main_file:
            continue
        yield child

def first_token(cursor):
    token = cursor.get_tokens().next()
    yield translate_token(token)

def first_node(cursor):
    for child in cursor.get_children():
        yield child
        break
    
def inc_indent(cursor):
    global indent_level
    indent_level += INDENT_SIZE
    return []
        
def indent(cursor):
    return " "*indent_level

def kind(cursor):
    return str(cursor.kind)


def location(nibble):
    return nibble.location


def matching_child(cursor):
    for c in cursor.get_children():
        if c.spelling == cursor.spelling:
            yield c
    
    
def nodes_and_tokens(cursor):
    children = cursor.get_children()
    tokens = cursor.get_tokens()
    try:
        t = tokens.next()
    except StopIteration:
        t = None
    for c in children:
        # Emit tokens preceding child
        l1 = c.extent.start.line
        c1 = c.extent.start.column
        while token_precedes(t, l1, c1):
            yield string_for_token(t)
            try:
                t = tokens.next()        
            except StopIteration:
                t = None
        yield c
        # Discard tokens inside child
        l1 = c.extent.end.line
        c1 = c.extent.end.column + 1
        while token_precedes(t, l1, c1):
            try:
                t = tokens.next()        
            except StopIteration:
                t = None
        l0 = l1
        c0 = c1
    l1 = cursor.extent.end.line
    c1 = cursor.extent.end.column + 1
    while token_precedes(t, l1, c1):
        yield string_for_token(t)
        try:
            t = tokens.next()        
        except StopIteration:
            t = None

def non_first_nodes(cursor):
    saw_first = False
    for child in cursor.get_children():
        if not saw_first:
            saw_first = True
            continue
        yield child
    

def show_whole_structure(cursor, my_indent=indent_level):
    result = " "*my_indent + "%s:%s:%s\n" % (cursor.kind, cursor.spelling, cursor.displayname)
    for child in cursor.get_children():
        result += show_whole_structure(child, my_indent + 4)
    return result

    
def spelling(cursor):
    return cursor.spelling    


def string_for_token(token):
    # return "%s'%s'" % (token.kind, token.spelling)
    return translate_token(token)
    
    
def token_precedes(token, line1, col1):
    if token is None:
        return False
    if token.location.line < line1:
        return True
    elif token.location.line == line1 and token.location.column < col1:
        return True
    else:
        return False


def translate_method(cursor):
    if cursor.spelling in method_translator:
        return method_translator[cursor.spelling]
    return cursor.spelling

 
def translate_token(token):
    if token.kind == TokenKind.PUNCTUATION:
        if token.spelling in punctuation_translator:
            return punctuation_translator[token.spelling]
    if token.kind == TokenKind.KEYWORD:
        if token.spelling in keyword_translator:
            return keyword_translator[token.spelling]
    return token.spelling

def translate_tokens(tokens):
    result = ""
    for t in tokens:
        result += translate_token(t)
    return result


def string_for_cursor(cursor):
    if isinstance(cursor, basestring):
        return cursor # It's already a string
    try:
        rules = cursor_sequence[cursor.kind]
    except KeyError: # ...undocumented cursor type...?
        rules = default_sequence
    result = ""
    for r in rules:
        if isinstance(r, basestring):
            result += r
        else:
            for child in r(cursor):
                result += string_for_cursor(child)
    return result
    

def token_comment(token, indent=0):
    c = str(token.spelling)
    if c.startswith('/*'):
        c = re.sub(r'^/\*', '#', c)
        for line in c.split('\n'):
            yield '#'
            yield line
            yield '\n'
    elif c.startswith("//"):
        c = re.sub(r"^//", "##", c)
        yield c
        yield '\n'
    else:
        raise "Unexpected comment %s" % token.spelling


def token_keyword(token):
    if token.spelling in keyword_translator:
        yield keyword_translator[token.spelling]
    else:
        yield token.spelling
        yield ' '


def token_punctuation(token, indent=0):
    if token.spelling in punctuation_translator:
        yield punctuation_translator[token.spelling]
    else:
        yield token.spelling
        
                
rules = {
    CursorKind.CLASS_DECL: [
            '\n', '\n', 
            'class', ' ', spelling, '(',
            class_bases,
            ')', ':', '\n',
            cursor_all_strings],
    TokenKind.COMMENT: [token_comment],
    TokenKind.KEYWORD: [token_keyword],
    TokenKind.PUNCTUATION: [token_punctuation],
    }


def main():
    # osg_src_dir = "F:/Users/cmbruns/build/OpenSceneGraph-3.2.1/OpenSceneGraph-3.2.1/"
    osg_src_dir = "C:/Users/cmbruns/git/osg/"
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
