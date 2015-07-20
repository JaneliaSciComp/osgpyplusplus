#!/bin/env python

# Module to help convert OpenSceneGraph C++ examples to python

import os
import re

import clang.cindex
from clang.cindex import CursorKind, TokenKind

INDENT_SIZE = 4

# Conversion from C++ to python
punctuation_dict = {
    '->': '.',
    '::': '.',
    '{': '',
    '}': '',
}

# Conversion from C++ to python
method_dict = {
    'operator()': '__call__',
}

def py_type(cursor):
    "Convert C++ type reference to python type name"
    t = ""
    for token in cursor.get_tokens():
        if token.kind == TokenKind.KEYWORD:
            continue # no keywords, like "public"
        elif token.kind == TokenKind.IDENTIFIER:
            t += token.spelling
        elif token.spelling in punctuation_dict and token.kind == TokenKind.PUNCTUATION:
            t += punctuation_dict[token.spelling]
        else:
            t += token.spelling # TODO??
            # print token.kind, token.spelling # TODO
    return t

def dump_tokens(cursor):
    for token in cursor.get_tokens():
        print token.kind, token.spelling, token.location.line, token.location.column


class CppBlock(object):
    "Base class for parsed C++ AST tree elements, to be translated to python"
    def __init__(self, cursor):
        self.cursor = cursor
        self.contents = list()
        self.next_indent = INDENT_SIZE
        child_ix = 0
        for c in cursor.get_children():
            n = self.handle_child(c, child_ix)
            child_ix += 1
            if n is None:
                pass
            else:
                self.contents.append(n)

    def gen_header_fragment(self, indent):
        return ""

    def gen_footer_fragment(self, indent):
        return ""

    def gen_py_fragment(self, indent):
        result = ""
        result += self.gen_header_fragment(indent)
        for f in self.contents:
            result += f.gen_py_fragment(indent + self.next_indent)
        result += self.gen_footer_fragment(indent)
        return result

    def handle_child(self, child, child_ix):
        if False:
            pass
        elif child.kind == CursorKind.COMPOUND_STMT:
            return CppCompoundStatement(child)
        elif child.kind == CursorKind.CALL_EXPR:
            return CppCallExpression(child)
        elif child.kind == CursorKind.DECL_STMT:
            return CppStatement(child)
        elif child.kind == CursorKind.RETURN_STMT:
            return CppReturnStatement(child)
        elif child.kind == CursorKind.MEMBER_REF_EXPR:
            return CppMemberRefExpression(child)
        return CppUnhandledNode(child)


class CppParammed(CppBlock):
    def __init__(self, cursor):
        self.params = []
        super(CppParammed, self).__init__(cursor)

    def gen_param_fragment(self, static=True):
        params1 = []
        if not static:
            params1.append("self")
        for param in self.params:
            params1.append(param.spelling)
        py_string = ""
        if len(params1) > 0:           
            py_string += ", ".join(params1)
        return py_string

    def handle_child(self, child, child_ix):
        if child.kind == CursorKind.PARM_DECL:
            self.params.append(child)
            return None
        else:
            return CppBlock.handle_child(self, child, child_ix)


class CppBaseMethod(CppParammed):
    def __init__(self, cursor):
        super(CppBaseMethod, self).__init__(cursor)

    def gen_footer_fragment(self, indent):
        return " "*indent + "\n" # Extra newline after methods


class CppCallExpression(CppBlock):
    def __init__(self, cursor):
        super(CppCallExpression, self).__init__(cursor)
        self.next_indent = 0 # no indentation inside compound statement

    def gen_py_fragment(self, indent):
        if len(self.contents) < 1:
            return "\nEMPTY_CALL?!"
        args = ""
        if len(self.contents) > 1:
            args = ", ".join([a.gen_py_fragment(indent) for a in self.contents[1:]])
        result = self.contents[0].gen_py_fragment(indent) + "(" + args + ")"
        return result
    

class CppCompoundStatement(CppBlock):
    def __init__(self, cursor):
        super(CppCompoundStatement, self).__init__(cursor)
        self.next_indent = 0 # no indentation inside compound statement


class CppConstructor(CppBaseMethod):
    def __init__(self, cursor):
        super(CppConstructor, self).__init__(cursor)

    def gen_header_fragment(self, indent):
        py_string = " "*indent + "def __init__("
        py_string += self.gen_param_fragment(False) # ctor is never static
        py_string += "):\n"
        # TODO initialize fields
        # TODO parent constructor
        return py_string

    def handle_child(self, child, child_ix):
        if child.kind == CursorKind.MEMBER_REF:
            return CppFieldLInit(child)
        elif child.kind == CursorKind.CALL_EXPR:
            return CppFieldRInit(child)
        else:
            return CppBaseMethod.handle_child(self, child, child_ix)


class CppClass(CppBlock):
    "Represents a class definition within a C++ source file to be translated"
    def __init__(self, cursor):
        self.base_classes = []
        self.fields = dict() # TODO - insert into constructors
        super(CppClass, self).__init__(cursor)

    def gen_header_fragment(self, indent):
        py_string = "\n" + " "*indent + "class " + self.cursor.spelling + "("
        bases = ", ".join([py_type(b) for b in self.base_classes])
        if len(self.base_classes) < 1:
            bases = "object"
        py_string += bases + "):\n\n"
        return py_string # emit class declaration python code, including newline

    def gen_py_fragment(self, indent):
        # Emit a class declaration
        result = ""
        result += self.gen_header_fragment(indent)
        for f in self.contents:
            result += f.gen_py_fragment(indent + 4)
        return result

    def handle_child(self, child, child_ix):
        if False:
            pass
        elif child.kind == CursorKind.CONSTRUCTOR:
            return CppConstructor(child)
        elif child.kind == CursorKind.CXX_ACCESS_SPEC_DECL:
            return None # Don't care about "public:" in python...
        elif child.kind == CursorKind.CXX_BASE_SPECIFIER:
            # find base class name
            self.base_classes.append(child)
            return None
        elif child.kind == CursorKind.CXX_METHOD:
            return CppMethod(child)
        elif child.kind == CursorKind.FIELD_DECL:
            self.fields[child.spelling] = child
            return None
        else:
            return CppUnhandledNode(child)


class CppFieldLInit(CppBlock):
    "left side of member field initializer expression"
    def __init__(self, cursor):
        super(CppFieldLInit, self).__init__(cursor)

    def gen_py_fragment(self, indent):
        return " "*indent + "self." + self.cursor.spelling + " = "


class CppFieldRInit(CppBlock):
    "right side of member field initializer expression"
    def __init__(self, cursor):
        c2 = cursor.get_children().next()
        super(CppFieldRInit, self).__init__(c2)

    def gen_py_fragment(self, indent):
        return self.cursor.spelling + "\n"


class CppFunction(CppBaseMethod):
    def __init__(self, cursor):
        super(CppFunction, self).__init__(cursor)

    def gen_header_fragment(self, indent):
        py_string = " "*indent + "def "
        method = str(self.cursor.spelling)
        py_string += method + "("
        py_string += self.gen_param_fragment()
        py_string += "):\n"
        return py_string


class CppMemberRefExpression(CppBlock):
    def __init__(self, cursor):
        super(CppMemberRefExpression, self).__init__(cursor)
        self.next_indent = 0
        
    def gen_footer_fragment(self, indent):
        return "." + self.cursor.spelling


class CppMethod(CppBaseMethod):
    def __init__(self, cursor):
        super(CppMethod, self).__init__(cursor)

    def gen_header_fragment(self, indent):
        py_string = " "*indent + "def "
        method = str(self.cursor.spelling)
        if method in method_dict:
            method = method_dict[method]
        py_string += method + "("        
        py_string += self.gen_param_fragment(self.cursor.is_static_method())
        py_string += "):\n"
        return py_string


class CppSourceFile(CppBlock):
    "Represents a C++ source file we want to convert to python"
    def __init__(self, file_name, args):
        self.index = clang.cindex.Index.create()
        translation_unit = self.index.parse(file_name, args)
        self.main_file = translation_unit.spelling
        super(CppSourceFile, self).__init__(translation_unit.cursor)
        self.next_indent = 0 # Don't indent main file contents

    def find_namespaces(self, cursor):
        "enumerate all namespaces, such as 'osg::', used in this file, to help enumerate python imports"
        ns = set()
        if (str(cursor.location.file).strip() == self.main_file) and (
                cursor.kind == CursorKind.NAMESPACE_REF):
            ns.add(str(cursor.spelling))
        for c in cursor.get_children():
            ns2 = self.find_namespaces(c)
            ns.update(ns2)
        return ns

    def gen_comment_fragment(self, indent=0):
        result = ""
        # Only display comments here that occur before the first semantic content,
        # i.e. module comments
        max_line = None
        if len(self.contents) > 0:
            max_line = self.contents[0].cursor.location.line
        for token in self.cursor.get_tokens():
            if token.kind != TokenKind.COMMENT:
                continue
            if max_line and token.location.line >= max_line:
                break
            c = token.spelling
            if c.startswith("/*"):
                c = re.sub(r"^/\*", "##", c)
                c = re.sub(r"\*/$", "##", c)
                c = re.sub(r"\n", "\n#", c)
            elif c.startswith("//"):
                c = re.sub(r"^//", "##", c)
            else:
                raise "Unexpected comment %s" % token.spelling
            c += "\n"
            result += c
        if len(result) > 0:
            result = "\n"+result # precede with blank line
        return result

    def gen_header_fragment(self, indent=0):
        result = ""
        result += "#!/bin/env python\n"
        result += "\n# OpenSceneGraph example program '%s' converted to python from C++\n" % (
            os.path.split(self.main_file)[1])
        c = self.gen_comment_fragment(indent)
        result += c
        imported = False
        local_namespaces = sorted(self.find_namespaces(self.cursor))
        for ns in local_namespaces:
            if ns.startswith("osg"):
                if not imported:
                    result += "\n" # one blank line before imports
                result += "from osgpypp import %s\n" % ns
                imported = True
        if imported:
            result += "\n" # one blank line after imports
        return result

    def handle_child(self, child, child_ix):
        # Only parse things found in this file
        if str(child.location.file).strip() != self.main_file:
            return None
        if child.kind == CursorKind.CLASS_DECL:
            return CppClass(child)
        elif child.kind == CursorKind.FUNCTION_DECL:
            return CppFunction(child)
        else:
            return CppBlock.handle_child(self, child, child_ix)


class CppStatement(CppBlock):
    def __init__(self, cursor):
        super(CppStatement, self).__init__(cursor)
        self.next_indent = 0
    
    def gen_footer_fragment(self, indent):
        return "\n" # end statement with a newline
    
    def gen_header_fragment(self, indent):
        return " "*indent # begin statement with indentation


class CppReturnStatement(CppStatement):
    def __init__(self, cursor):
        super(CppReturnStatement, self).__init__(cursor)
    
    def gen_header_fragment(self, indent):
        return " "*indent + "return " # begin statement with indentation


class CppUnhandledNode(CppBlock):
    "Placeholder for syntax tree object I have not wrapped/handled yet"
    def __init__(self, cursor):
        super(CppUnhandledNode, self).__init__(cursor)

    def gen_header_fragment(self, indent):
        child = self.cursor
        return "%s[%s]" % (child.spelling, child.kind)
        return "%s!!! *** Unrecognized node type %s %s %s\n" % (
            " "*indent,
            child.kind, 
            child.spelling, 
            child.displayname)

def main():
    examples_src = "C:/Users/cmbruns/git/osg/examples"
    osg_includes = "C:/Users/cmbruns/git/osg/include"
    src_file = examples_src + "/osggraphicscost/osggraphicscost.cpp"
    src_obj = CppSourceFile(src_file, args=["-I%s"%osg_includes, 'c++'] )
    print src_obj.gen_py_fragment(0)


if __name__ == "__main__":
    main()
