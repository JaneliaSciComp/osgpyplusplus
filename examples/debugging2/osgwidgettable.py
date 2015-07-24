#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgettable"

import sys
from osgpypp import osgWidget

# Translated from file 'osgwidgettable.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgettable.cpp 43 2008-04-17 03:40:05Z cubicool $

MASK_2D = 0xF0000000

# This examples demonstrates the use of an osgWidget.Table, which differs from a Box in
# many ways. First and foremost, a Table's size is intially known, whereas a Box can be
# dynamically added to. Secondly, a table is matrix Layout, with both vertical and
# horizontal placement cells. A Box, on the other hand, can only be vertical or horizontal.

def main(argv):
    viewer = osgViewer.Viewer()
    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    table = osgWidget.Table("table", 3, 3)
    # Here we create our "cells" manually, though it will often be convenient to
    # do so algorithmically. Also, notice how we set the text name of each widget to
    # correspond with it's "index" in the table. This is merely a convenience, which
    # we use later...
    table.addWidget(osgWidget.Widget("0, 0", 100.0, 25.0), 0, 0)
    table.addWidget(osgWidget.Widget("0, 1", 100.0, 25.0), 0, 1)
    table.addWidget(osgWidget.Widget("0, 2", 100.0, 75.0), 0, 2)
    table.addWidget(osgWidget.Widget("1, 0", 200.0, 45.0), 1, 0)
    table.addWidget(osgWidget.Widget("1, 1", 200.0, 45.0), 1, 1)
    table.addWidget(osgWidget.Widget("1, 2", 200.0, 45.0), 1, 2)
    table.addWidget(osgWidget.Widget("2, 0", 300.0, 65.0), 2, 0)
    table.addWidget(osgWidget.Widget("2, 1", 300.0, 65.0), 2, 1)
    table.addWidget(osgWidget.Widget("2, 2", 300.0, 65.0), 2, 2)
    table.getBackground().setColor(0.0, 0.0, 0.5, 1.0)
    table.attachMoveCallback()
    # Use a hackish method of setting the spacing for all Widgets.
    for i in table:
        # for(osgWidget.Table.Iterator i = table.begin() i != table.end() i++)
        i.setPadding(1.0)
    # Now we fetch the very first 0, 0 Widget in the table using an awkward method.
    # This is merely one way to fetch a Widget from a Window, there are many others.
    # The osgWidget.Window.getByName interface will be very handy in scripting languages
    # where users will want to retrieve handles to existing Windows using a useful
    # textual name, such as "MainGUIParent" or something.
    table.getByName("0, 0").setAlignHorizontal(osgWidget.Widget.HA_LEFT)
    table.getByName("0, 0").setAlignVertical(osgWidget.Widget.VA_BOTTOM)
    table.getByName("0, 0").setPadLeft(50.0)
    table.getByName("0, 0").setPadTop(3.0)
    # Change the colors a bit to differentiate this row from the others.
    table.getByName("2, 0").setColor(1.0, 0.0, 0.0, 1.0, osgWidget.Widget.LOWER_LEFT)
    table.getByName("2, 1").setColor(1.0, 0.0, 0.0, 0.5)
    table.getByName("2, 2").setColor(1.0, 0.0, 0.0, 0.5)
    wm.addChild(table)
    createExample = return(viewer, wm)

if __name__ == "__main__":
    main(sys.argv)
