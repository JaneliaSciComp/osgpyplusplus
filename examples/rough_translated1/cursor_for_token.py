#!/bin/env python

# Tool for debugging clang translator

import sys

import clang.cindex

def cursors_with_token(cursor, token):
    for t in cursor.get_tokens():
        if token in t.spelling:
            yield cursor
            break
    for child in cursor.get_children():
        for c in cursors_with_token(child, token):
            yield c

def cursor_for_token(token, source):
    examples_src = "C:/Users/cmbruns/git/osg/examples"
    osg_includes = "C:/Users/cmbruns/git/osg/include"
    src_file = examples_src + "/"+source+"/"+source+".cpp"
    index = clang.cindex.Index.create()
    translation_unit = index.parse(src_file, args=["-I%s"%osg_includes, 'c++'])
    for child in translation_unit.cursor.get_children():
        # if str(child.location.file) != translation_unit.spelling:
        #     continue
        for cursor in cursors_with_token(child, token):
            yield cursor

if __name__ == "__main__":
    token = sys.argv[1]
    source = sys.argv[2]
    for cursor in cursor_for_token(token, source):
        s = cursor.extent.start
        e = cursor.extent.end
        print "%s %d.%d-%d.%d" % (cursor.kind, s.line, s.column, e.line, e.column)
