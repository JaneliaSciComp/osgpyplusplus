#!/bin/env python

# Module to help convert OpenSceneGraph C++ examples to python

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
    return ["ARGS...",]

def bases(class_cursor):
    bases = []
    for c in class_cursor.get_children():
        if c.kind == CursorKind.CXX_BASE_SPECIFIER:
            bases.append(c)
    args = ", ".join([string_for_cursor(b) for b in bases])
    if len(bases) < 1:
        args = "object"
    yield "(" + args + ")"

def debug(cursor):
    yield cursor.kind

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
    yield cursor.get_tokens().next().spelling

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

def non_first_nodes(cursor):
    saw_first = False
    for child in cursor.get_children():
        if not saw_first:
            saw_first = True
            continue
        yield child
    
def matching_child(cursor):
    for c in cursor.get_children():
        if c.spelling == cursor.spelling:
            yield c
    
def spelling(cursor):
    return cursor.spelling    

default_sequence = [indent, "**", kind, ":", spelling, ":", displayname, "\n", inc_indent, all_nodes, dec_indent]
# 
cursor_sequence = {
    CursorKind.CALL_EXPR: [matching_child, "(", arg_nonmatching, ")"],
    CursorKind.CLASS_DECL: [indent, "class ", spelling, bases, ":\n", inc_indent, all_nodes, dec_indent],
    CursorKind.COMPOUND_STMT: [all_nodes], 
    # CursorKind.CONSTRUCTOR: [indent, "def __init__", args, ":\n"],
    CursorKind.CXX_ACCESS_SPEC_DECL: [all_nodes], # Don't care about "public:" in python...
    CursorKind.CXX_BASE_SPECIFIER: [all_nodes],
    # CursorKind.CXX_METHOD: [all_nodes],
    CursorKind.DECL_REF_EXPR: [spelling, all_nodes], # TODO not sure about the all_nodes...
    CursorKind.DECL_STMT: [indent, all_nodes, "\n"],
    # CursorKind.FIELD_DECL: [],
    # CursorKind.FUNCTION_DECL: [], # [indent, "def ", spelling, args, ":\n"], # TODO
    CursorKind.IF_STMT: [indent, "if ", first_node, ":\n", inc_indent, non_first_nodes, dec_indent, "\n"],
    CursorKind.INTEGER_LITERAL: [first_token],
    CursorKind.MEMBER_REF_EXPR: [all_nodes, ".", spelling],
    # CursorKind.MEMBER_REF: [".", spelling],
    CursorKind.NAMESPACE_REF: [spelling, ".", all_nodes],
    # CursorKind.PARM_DECL: [spelling, all_nodes],
    CursorKind.RETURN_STMT: [indent, "return ", all_nodes, "\n"],
    CursorKind.TRANSLATION_UNIT: [filter_by_file],
    CursorKind.TYPE_REF: [py_type, all_nodes],
    CursorKind.UNEXPOSED_EXPR: [all_nodes],
}

def string_for_cursor(cursor):
    result = ""
    try: # Is argument a cursor...?
        rules = cursor_sequence[cursor.kind]
    except KeyError: # ...undocumented cursor type...?
        rules = default_sequence
    except AttributeError: # ...or a string?
        return cursor
    for r in rules:
        try: # is it a string...?
            result += r + ""
        except TypeError: # ...or a function?
            for child in r(cursor):
                result += string_for_cursor(child)
    return result
    

def main():
    examples_src = "C:/Users/cmbruns/git/osg/examples"
    osg_includes = "C:/Users/cmbruns/git/osg/include"
    src_file = examples_src + "/osggraphicscost/osggraphicscost.cpp"
    index = clang.cindex.Index.create()
    translation_unit = index.parse(src_file, args=["-I%s"%osg_includes, 'c++'])
    global main_file
    main_file = str(translation_unit.spelling)
    print string_for_cursor(translation_unit.cursor)


if __name__ == "__main__":
    main()
