#!/bin/env python

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
            print token.kind, token.spelling # TODO
    return t


class CppBlock(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.contents = list()
        for c in cursor.get_children():
            n = self.handle_child(c)
            if n is not None:
                self.contents.append(n)

    def gen_decl_fragment(self, indent):
        return ""

    def gen_py_fragment(self, indent):
        result = ""
        result += self.gen_decl_fragment(indent)
        for f in self.contents:
            result += f.gen_py_fragment(indent + 4)
        return result

    def handle_child(self, child):
        return CppUnhandledNode(child)


class CppConstructor(CppBlock):
    def __init__(self, cursor):
        CppBlock.__init__(self, cursor)

    def gen_decl_fragment(self, indent):
        params = ["self"]
        for param in self.cursor.get_children():
            if param.kind == CursorKind.PARM_DECL:
                params.append(param.spelling)
        py_string = "\n" + " "*indent + "def __init__("
        py_string += ", ".join(params)
        py_string += "):\n"
        return py_string


class CppClass(CppBlock):
    "Represents a class definition within a C++ source file to be translated"
    def __init__(self, cursor):
        self.base_classes = []
        self.fields = dict() # TODO - insert into constructors
        CppBlock.__init__(self, cursor)

    def gen_decl_fragment(self, indent):
        py_string = "\n" + " "*indent + "class " + self.cursor.spelling + "("
        bases = ", ".join([py_type(b) for b in self.base_classes])
        if len(self.base_classes) < 1:
            bases = "object"
        py_string += bases + "):\n"
        return py_string # emit class declaration python code, including newline

    def gen_py_fragment(self, indent):
        # Emit a class declaration
        result = ""
        result += self.gen_decl_fragment(indent)
        for f in self.contents:
            result += f.gen_py_fragment(indent + 4)
        return result

    def handle_child(self, child):
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


class CppFunction(CppBlock):
    def __init__(self, cursor):
        CppBlock.__init__(self, cursor)

    def gen_decl_fragment(self, indent):
        py_string = "\n" + " "*indent + "def "
        method = str(self.cursor.spelling)
        py_string += method + "("
        params = []
        for param in self.cursor.get_children():
            if param.kind == CursorKind.PARM_DECL:
                params.append(param.spelling)
        if len(params) > 0:           
            py_string += ", ".join(params)
        py_string += "):\n"
        return py_string


class CppMethod(CppBlock):
    def __init__(self, cursor):
        CppBlock.__init__(self, cursor)

    def gen_decl_fragment(self, indent):
        py_string = "\n" + " "*indent + "def "
        method = str(self.cursor.spelling)
        if method in method_dict:
            method = method_dict[method]
        py_string += method + "("
        params = []
        if not self.cursor.is_static_method():
            params.append("self")
        for param in self.cursor.get_children():
            if param.kind == CursorKind.PARM_DECL:
                params.append(param.spelling)
        if len(params) > 0:           
            py_string += ", ".join(params)
        py_string += "):\n"
        return py_string


class CppSourceFile(CppBlock):
    "Represents a C++ source file we want to convert to python"
    def __init__(self, file_name, args):
        self.index = clang.cindex.Index.create()
        translation_unit = self.index.parse(file_name, args)
        self.main_file = translation_unit.spelling
        CppBlock.__init__(self, translation_unit.cursor)

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

    def gen_import_fragment(self):
        result = ""
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

    def gen_py_file(self):
        result = ""
        result += self.gen_import_fragment()
        result += walk_tree(self.cursor, self.main_file)
        return result

    def handle_child(self, child):
        # Only parse things found in this file
        if str(child.location.file).strip() != self.main_file:
            return None
        if child.kind == CursorKind.CLASS_DECL:
            return CppClass(child)
        elif child.kind == CursorKind.FUNCTION_DECL:
            return CppFunction(child)
        else:
            return CppUnhandledNode(child)


class CppUnhandledNode(CppBlock):
    def __init__(self, cursor):
        CppBlock.__init__(self, cursor)

    def gen_decl_fragment(self, indent):
        child = self.cursor
        return "%sUnrecognized node type %s %s %s\n" % (
            " "*indent,
            child.kind, 
            child.spelling, 
            child.displayname)


def walk_tree(cursor, main_file, indent = 0):
    result = ""
    # Only emit declarations that are in our file of interest
    if str(cursor.location.file).strip() == main_file:
        if False:
            pass
        elif cursor.kind == CursorKind.CXX_ACCESS_SPEC_DECL:
            pass # ignore "public:"
        elif cursor.kind == CursorKind.CLASS_DECL:
            cls = CppClass(cursor)
            result += cls.gen_py_fragment(indent)
            return result
        elif cursor.kind == CursorKind.CONSTRUCTOR:
            params = ["self"]
            for param in cursor.get_children():
                if param.kind == CursorKind.PARM_DECL:
                    params.append(param.spelling)
            py_string = "\n" + " "*indent + "def __init__("
            py_string += ", ".join(params)
            py_string += "):\n"
            result += py_string
            indent += 4
        elif cursor.kind == CursorKind.CXX_BASE_SPECIFIER:
            pass # already handled in constructor
            return result # skip substructure
        elif cursor.kind == CursorKind.CXX_METHOD:
            py_string = "\n" + " "*indent + "def "
            method = str(cursor.spelling)
            if method in method_dict:
                method = method_dict[method]
            py_string += method + "("
            params = []
            if not cursor.is_static_method():
                params.append("self")
            for param in cursor.get_children():
                if param.kind == CursorKind.PARM_DECL:
                    params.append(param.spelling)
            if len(params) > 0:           
                py_string += ", ".join(params)
            py_string += "):\n"
            result += py_string
            indent += 4
        elif cursor.kind == CursorKind.FUNCTION_DECL:
            py_string = "\n" + " "*indent + "def "
            py_string += cursor.spelling + "("
            params = []
            for param in cursor.get_children():
                if param.kind == CursorKind.PARM_DECL:
                    params.append(param.spelling)
            if len(params) > 0:           
                py_string += ", ".join(params)
            py_string += "):\n"
            result += py_string
            indent += 4
        else:
            result += " "*indent + str(cursor.kind) + ", " + cursor.spelling + ", " + cursor.displayname + "\n"
            for c in cursor.get_children():
                result += walk_tree(c, main_file, indent+1)
            return result
    for c in cursor.get_children():
        result += walk_tree(c, main_file, indent)
    return result

if __name__ == "__main__":
    examples_src = "C:/Users/cmbruns/git/osg/examples"
    osg_includes = "C:/Users/cmbruns/git/osg/include"
    src_file = examples_src + "/osggraphicscost/osggraphicscost.cpp"
    src_obj = CppSourceFile(src_file, args=["-I%s"%osg_includes, 'c++'] )
    print src_obj.gen_py_fragment(0)

