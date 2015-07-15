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

def find_namespaces(cursor, main_file):
    "enumerate all namespaces, such as 'osg::', used in this file, to help enumerate python imports"
    ns = set()
    if (str(cursor.location.file).strip() == main_file) and (
            cursor.kind == CursorKind.NAMESPACE_REF):
        ns.add(str(cursor.spelling))
    for c in cursor.get_children():
        ns2 = find_namespaces(c, main_file)
        ns.update(ns2)
    return ns

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
            print token.kind, token.spelling
    return t

def walk_tree(cursor, main_file, indent = 0):
    # Only emit declarations that are in our file of interest
    if str(cursor.location.file).strip() == main_file:
        if False:
            pass
        elif cursor.kind == CursorKind.CXX_ACCESS_SPEC_DECL:
            pass # ignore "public:"
        elif cursor.kind == CursorKind.CLASS_DECL:
            # Emit a class declaration
            # find base class name
            base_classes = []
            for base in cursor.get_children():
                if base.kind == CursorKind.CXX_BASE_SPECIFIER:
                    base_classes.append(base)
            py_string = "\n" + " "*indent + "class " + cursor.spelling + "("
            bases = ", ".join([py_type(b) for b in base_classes])
            if len(base_classes) < 1:
                bases = "object"
            py_string += bases + "):\n" # extra newline for class
            print py_string # emit class declaration python code, including newline
            indent += 4
        elif cursor.kind == CursorKind.CONSTRUCTOR:
            params = ["self"]
            for param in cursor.get_children():
                if param.kind == CursorKind.PARM_DECL:
                    params.append(param.spelling)
            py_string = " "*indent + "def __init__("
            py_string += ", ".join(params)
            py_string += "):"
            print py_string
            indent += 4
        elif cursor.kind == CursorKind.CXX_BASE_SPECIFIER:
            pass # already handled in constructor
            return
        else:
            print " "*indent + str(cursor.kind), cursor.spelling, cursor.displayname
    for c in cursor.get_children():
        walk_tree(c, main_file, indent)

examples_src = "C:/Users/cmbruns/git/osg/examples"
osg_includes = "C:/Users/cmbruns/git/osg/include"
index = clang.cindex.Index.create()
src_file = examples_src + "/osggraphicscost/osggraphicscost.cpp"
translation_unit = index.parse(src_file, args=["-I%s"%osg_includes, 'c++'] )
cursor = translation_unit.cursor
print dir(cursor)
main_file = translation_unit.spelling

namespaces = sorted(find_namespaces(cursor, main_file))
imported = False
for ns in namespaces:
    if ns.startswith("osg"):
        if not imported:
            print # one blank line before imports
        print "from osgpypp import %s" % ns
        imported = True
if imported:
    print # one blank line after imports

walk_tree(cursor, main_file)

