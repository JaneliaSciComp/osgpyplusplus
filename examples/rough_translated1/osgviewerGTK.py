#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerGTK"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import gtk
from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osggtkdrawingarea.cpp'

#include "osggtkdrawingarea.h"

OSGGTKDrawingArea.OSGGTKDrawingArea():
_widget   (gtk_drawing_area_new()),
_glconfig (0),
_context  (0),
_drawable (0),
_state    (0),
_queue    (*getEventQueue()) 
    setCameraManipulator(osgGA.TrackballManipulator())

OSGGTKDrawingArea.~OSGGTKDrawingArea() 

bool OSGGTKDrawingArea.createWidget(int width, int height) 
    _glconfig = gdk_gl_config_new_by_mode(static_cast<GdkGLConfigMode>(
        GDK_GL_MODE_RGBA |
        GDK_GL_MODE_DEPTH |
        GDK_GL_MODE_DOUBLE
    ))

    if not _glconfig : 
        osg.notify(osg.FATAL), "Fail not "

        return False

    gtk_widget_set_size_request(_widget, width, height)

    gtk_widget_set_gl_capability(
        _widget,
        _glconfig,
        0,
        True,
        GDK_GL_RGBA_TYPE
    )

    gtk_widget_add_events(
        _widget,
        GDK_BUTTON1_MOTION_MASK |
        GDK_BUTTON2_MOTION_MASK |
        GDK_BUTTON3_MOTION_MASK |
        GDK_POINTER_MOTION_MASK |
        GDK_BUTTON_PRESS_MASK |
        GDK_BUTTON_RELEASE_MASK |
        GDK_KEY_PRESS_MASK |
        GDK_KEY_RELEASE_MASK |
        GDK_VISIBILITY_NOTIFY_MASK
    )

    # We do this so that we don't have to suck up ALL the input to the
    # window, but instead just when the drawing area is focused.
    g_object_set(_widget, "can-focus", True, NULL)

    _connect("realize", G_CALLBACK(OSGGTKDrawingArea._srealize))
    _connect("unrealize", G_CALLBACK(OSGGTKDrawingArea._sunrealize))
    _connect("expose_event", G_CALLBACK(OSGGTKDrawingArea._sexpose_event))
    _connect("configure_event", G_CALLBACK(OSGGTKDrawingArea._sconfigure_event))
    _connect("motion_notify_event", G_CALLBACK(OSGGTKDrawingArea._smotion_notify_event))
    _connect("button_press_event", G_CALLBACK(OSGGTKDrawingArea._sbutton_press_event))
    _connect("button_release_event", G_CALLBACK(OSGGTKDrawingArea._sbutton_press_event))
    _connect("key_press_event", G_CALLBACK(OSGGTKDrawingArea._skey_press_event))

    _gw = setUpViewerAsEmbeddedInWindow(0, 0, width, height)

    return True

void OSGGTKDrawingArea._realize(GtkWidget* widget) 
    _context  = gtk_widget_get_gl_context(widget)
    _drawable = gtk_widget_get_gl_drawable(widget)

    gtkRealize()

void OSGGTKDrawingArea._unrealize(GtkWidget* widget) 
    gtkUnrealize()

bool OSGGTKDrawingArea._expose_event(GtkWidget* widget, GdkEventExpose* event) 
    if not gtkGLBegin() : return False

    frame()

    gtkGLSwap()
    gtkGLEnd()

    gtkExpose = return()

bool OSGGTKDrawingArea._configure_event(GtkWidget* widget, GdkEventConfigure* event) 
    gtkGLBegin()

    _queue.windowResize(0, 0, event.width, event.height)

    _gw.resized(0, 0, event.width, event.height)

    gtkGLEnd()

    gtkConfigure = return(event.width, event.height)

bool OSGGTKDrawingArea._motion_notify_event(GtkWidget* widget, GdkEventMotion* event) 
    _state = event.state

    _queue.mouseMotion(event.x, event.y)

    gtkMotionNotify = return(event.x, event.y)

bool OSGGTKDrawingArea._button_press_event(GtkWidget* widget, GdkEventButton* event) 
    _state = event.state

    if event.type == GDK_BUTTON_PRESS : 
        if event.button == 1 : gtk_widget_grab_focus(_widget)

        _queue.mouseButtonPress(event.x, event.y, event.button)

        gtkButtonPress = return(event.x, event.y, event.button)

    elif event.type == GDK_BUTTON_RELEASE : 
        _queue.mouseButtonRelease(event.x, event.y, event.button)

        gtkButtonRelease = return(event.x, event.y, event.button)

    else return False

bool OSGGTKDrawingArea._key_press_event(GtkWidget* widget, GdkEventKey* event) 
    _state = event.state

    if event.type == GDK_KEY_PRESS : 
        _queue.keyPress(event.keyval)

        gtkKeyPress = return(event.keyval)

    elif event.type == GDK_KEY_RELEASE : 
        _queue.keyRelease(event.keyval)

        gtkKeyRelease = return(event.keyval)

    else return False

# Translated from file 'osggtkdrawingarea.h'

#include <gtk/gtk.h>
#include <gtk/gtkgl.h>
#include <osgViewer/Viewer>
#include <osgGA/TrackballManipulator>

# This is an implementation of SimpleViewer that is designed to be subclassed
# and used as a GtkDrawingArea in a GTK application. Because of the implemention
# of GTK, I was unable to derive from GtkWidget and instead had to "wrap" it.
# Conceptually, however, you can think of an OSGGTKDrawingArea as both an OSG
# Viewer AND GtkDrawingArea.
#
# While it is possible to use this class directly, it won't end up doing anything
# interesting without calls to queueDraw, which ideally are done in the user's
# subclass implementation (see: osgviewerGTK).
class OSGGTKDrawingArea (osgViewer.Viewer) :
_widget = GtkWidget*()
    _glconfig = GdkGLConfig*()
    _context = GdkGLContext*()
    _drawable = GdkGLDrawable*()
    
    _gw = osgViewer.GraphicsWindowEmbedded()

    _state = unsigned int()

    _queue = osgGA.EventQueue()

    static OSGGTKDrawingArea* _self(gpointer self) 
        return static_cast<OSGGTKDrawingArea*>(self)

    # A simple helper function to connect us to the various GTK signals.
    def _connect(name, callback):
        
        g_signal_connect(G_OBJECT(_widget), name, callback, this)

    _realize = void(GtkWidget*)
    _unrealize = void(GtkWidget*)
    _expose_event = bool(GtkWidget*, GdkEventExpose*)
    _configure_event = bool(GtkWidget*, GdkEventConfigure*)
    _motion_notify_event = bool(GtkWidget*, GdkEventMotion*)
    _button_press_event = bool(GtkWidget*, GdkEventButton*)
    _key_press_event = bool(GtkWidget*, GdkEventKey*)

    # The following functions are static "wrappers" so that we can invoke the
    # bound methods of a class instance by passing the "this" pointer as the
    # self argument and invoking it explicitly.
    static void _srealize(GtkWidget* widget, gpointer self) 
        _self(self)._realize(widget)

    static void _sunrealize(GtkWidget* widget, gpointer self) 
        _self(self)._unrealize(widget)

    static bool _sexpose_event(GtkWidget* widget, GdkEventExpose* expose, gpointer self) 
        return _self(self)._expose_event(widget, expose)

    static bool _sconfigure_event(
        GtkWidget*         widget,
        GdkEventConfigure* event,
        gpointer           self
    ) 
        return _self(self)._configure_event(widget, event)

    static bool _smotion_notify_event(
        GtkWidget*      widget,
        GdkEventMotion* event,
        gpointer        self
    ) 
        return _self(self)._motion_notify_event(widget, event)

    static bool _sbutton_press_event(
        GtkWidget*      widget,
        GdkEventButton* event,
        gpointer        self
    ) 
        return _self(self)._button_press_event(widget, event)

    static bool _skey_press_event(
        GtkWidget*   widget,
        GdkEventKey* event,
        gpointer     self
    ) 
        return _self(self)._key_press_event(widget, event)
    # You can override these in your subclass if you'd like. :)
    # Right now they're fairly uninformative, but they could be easily extended.
    # Note that the "state" information isn't passed around to each function
    # but is instead stored and abstracted internally. See below.

    def gtkRealize():

        
    def gtkUnrealize():
        
    def gtkExpose():
        
        return True
    

    # The width and height.
    virtual bool gtkConfigure(int, int) 
        return True
    

    # The "normalized" coordinates of the mouse.
    virtual bool gtkMotionNotify(double, double) 
        return True
    

    # The "normalized" coordinates of the mouse and the mouse button code on down.
    virtual bool gtkButtonPress(double, double, unsigned int) 
        return True
    

    # The "normalized" coordinates of the mouse and mouse button code on release.
    virtual bool gtkButtonRelease(double, double, unsigned int) 
        return True

    # The X key value on down.
    def gtkKeyPress(int):
        
        return True
    

    # The X key value on release.
    def gtkKeyRelease(int):
        
        return True
    

    # These functions wrap state tests of the most recent state in the
    # GtkDrawingArea.

    inline bool stateShift() 
        return _state  GDK_SHIFT_MASK

    inline bool stateLock() 
        return _state  GDK_LOCK_MASK

    inline bool stateControl() 
        return _state  GDK_CONTROL_MASK

    inline bool stateMod() 
        return _state  (
            GDK_MOD1_MASK |
            GDK_MOD2_MASK |
            GDK_MOD3_MASK |
            GDK_MOD4_MASK |
            GDK_MOD5_MASK
        )

    inline bool stateButton() 
        return _state  (
            GDK_BUTTON1_MASK |
            GDK_BUTTON2_MASK |
            GDK_BUTTON3_MASK |
            GDK_BUTTON4_MASK |
            GDK_BUTTON5_MASK
        )
    OSGGTKDrawingArea  ()
    ~OSGGTKDrawingArea ()

    createWidget = bool(int, int)

    def getWidget():

        
        return _widget

    def gtkGLBegin():

        
        if _drawable and _context : return gdk_gl_drawable_gl_begin(_drawable, _context)

        else return False

    def gtkGLEnd():

        
        if _drawable : gdk_gl_drawable_gl_end(_drawable)

    # Because of GTK's internal double buffering, I'm not sure if we're really
    # taking advantage of OpenGL's internal swapping.
    def gtkGLSwap():
        
        if _drawable and gdk_gl_drawable_is_double_buffered(_drawable) : 
            gdk_gl_drawable_swap_buffers(_drawable)

            return True

        else:
            glFlush()

            return False

    def queueDraw():

        
        gtk_widget_queue_draw(_widget)


# Translated from file 'osgviewerGTK.cpp'

#include <string.h>

#include <iostream>
#include <string>
#include <osg/Stats>
#include <osgDB/ReadFile>

#include "osggtkdrawingarea.h"

HELP_TEXT = "Use CTRL or SHIFT plus right-click to pull up a fake menu.\n"
    "Use the standard TrackballManipulator keys to rotate the loaded\n"
    "model (with caveats the model won't keep rotating).\n"
    "\n"
    "<b>OpenSceneGraph Project, 2008</b>"


# If you want to see how to connect class method to callbacks, take a look at the
# implementation of OSGGTKDrawingArea. It's dirty, but it's the only way I could
# come up with.
bool activate(GtkWidget* widget, gpointer) 
    label = gtk_bin_get_child(GTK_BIN(widget))

    print "MENU: ", gtk_label_get_label(GTK_LABEL(label))

    return True

# Our derived OSGGTKDrawingArea "widget." Redraws occur while the mouse buttons
# are held down and mouse motion is detected.
#
# This is the easiest way to demonstrate the use of OSGGTKDrawingArea. We override
# a few of the event methods to setup our menu and to issue redraws. Note that an
# unmodified OSGGTKDrawingArea never calls queueDraw, so OSG is never asked to render
# itself.
class ExampleOSGGTKDrawingArea (OSGGTKDrawingArea) :
_menu = GtkWidget*()
    
    _tid = unsigned int()

    # A helper function to easily setup our menu entries.
    def _menuAdd(title):
        
        item = gtk_menu_item_new_with_label(title.c_str())
        
        gtk_menu_shell_append(GTK_MENU_SHELL(_menu), item)

        g_signal_connect(G_OBJECT(item), "activate", G_CALLBACK(activate), 0)

    def _clicked(widget):

        
        text = gtk_label_get_label(
            GTK_LABEL(gtk_bin_get_child(GTK_BIN(widget)))
        )

        if not strncmp(text, "Close", 5) : gtk_main_quit()
    
        elif not strncmp(text, "Open File", 9) : 
            of = gtk_file_chooser_dialog_new(
                "Please select an OSG file...",
                GTK_WINDOW(gtk_widget_get_toplevel(getWidget())),
                GTK_FILE_CHOOSER_ACTION_OPEN,
                GTK_STOCK_CANCEL,
                GTK_RESPONSE_CANCEL,
                GTK_STOCK_OPEN,
                GTK_RESPONSE_ACCEPT,
                NULL
            )

            if gtk_dialog_run(GTK_DIALOG(of)) == GTK_RESPONSE_ACCEPT : 
                file = gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(of))

                model = osgDB.readNodeFile(file)

                if model.valid() : 
                    setSceneData(model)
                
                    queueDraw()

                g_free(file)
            
            gtk_widget_destroy(of)

        # Assume we're wanting FPS toggling.
        else:
            if not _tid : 
                _tid = g_timeout_add(
                    15,
                    (GSourceFunc)(ExampleOSGGTKDrawingArea.timeout),
                    this
                )

                gtk_button_set_label(GTK_BUTTON(widget), "Toggle 60 FPS (off)")

            else:
                g_source_remove(_tid)
                gtk_button_set_label(GTK_BUTTON(widget), "Toggle 60 FPS (on)")

                _tid = 0

        return True
    # Check right-click release to see if we need to popup our menu.
    bool gtkButtonRelease(double, double, unsigned int button) 
        if button == 3 and (stateControl() or stateShift()) : gtk_menu_popup(
            GTK_MENU(_menu),
            0,
            0,
            0,
            0,
            button,
            0
        )

        return True

    # Our "main" drawing pump. Since our app is just a model viewer, we use
    # click+motion as our criteria for issuing OpenGL refreshes.
    bool gtkMotionNotify(double, double) 
        if stateButton() : queueDraw()

        return True
    ExampleOSGGTKDrawingArea():
    OSGGTKDrawingArea (),
    _menu             (gtk_menu_new()),
    _tid              (0) 
        _menuAdd("Option")
        _menuAdd("Another Option")
        _menuAdd("Still More Options")

        gtk_widget_show_all(_menu)

        getCamera().setStats(osg.Stats("omg"))

    ~ExampleOSGGTKDrawingArea() 

    # Public so that we can use this as a callback in main().
    static bool clicked(GtkWidget* widget, gpointer self) 
        return static_cast<ExampleOSGGTKDrawingArea*>(self)._clicked(widget)

    #static gboolean timeout(GtkWidget* widget) 
    static bool timeout(void* self) 
        static_cast<ExampleOSGGTKDrawingArea*>(self).queueDraw()

        return True


# Our main() function not  FINALLY not  Most of this code is GTK stuff, so it's mostly boilerplate.
# If we wanted to get real jiggy with it we could use Glade and cut down about 20 lines of
# code or so.
def main(argv):
    
    gtk_init(argc, argv)
    gtk_gl_init(argc, argv)

    da = ExampleOSGGTKDrawingArea()

    if da.createWidget(640, 480) : 
        if argc >= 2 : 
            model = osgDB.readNodeFile(argv[1])

            if model.valid() : da.setSceneData(model)

        window = gtk_window_new(GTK_WINDOW_TOPLEVEL)
        vbox1 = gtk_vbox_new(False, 3)
        vbox2 = gtk_vbox_new(False, 3)
        hbox = gtk_hbox_new(False, 3)
        label = gtk_label_new("")
        GtkWidget* buttons[] = 
            gtk_button_new_with_label("Open File"),
            gtk_button_new_with_label("Toggle 60 FPS (on)"),
            gtk_button_new_with_label("Close")
        

        gtk_label_set_use_markup(GTK_LABEL(label), True)
        gtk_label_set_label(GTK_LABEL(label), HELP_TEXT)

        for(unsigned int i = 0 i < sizeof(buttons) / sizeof(GtkWidget*) i++) 
            gtk_box_pack_start(
                GTK_BOX(vbox2),
                buttons[i],
                False,
                False,
                0
            )

            g_signal_connect(
                G_OBJECT(buttons[i]),
                "clicked",
                G_CALLBACK(ExampleOSGGTKDrawingArea.clicked),
                da
            )

        gtk_window_set_title(GTK_WINDOW(window), "osgviewerGTK")

        gtk_box_pack_start(GTK_BOX(hbox), vbox2, True, True, 2)
        gtk_box_pack_start(GTK_BOX(hbox), label, True, True, 2)

        gtk_box_pack_start(GTK_BOX(vbox1), da.getWidget(), True, True, 2)
        gtk_box_pack_start(GTK_BOX(vbox1), hbox, False, False, 2)

        gtk_container_set_reallocate_redraws(GTK_CONTAINER(window), True)
        gtk_container_add(GTK_CONTAINER(window), vbox1)

        g_signal_connect(
            G_OBJECT(window),
            "delete_event",
            G_CALLBACK(gtk_main_quit),
            0
        )

        gtk_widget_show_all(window)
        gtk_main()

    else return 1

    return 0


if __name__ == "__main__":
    main(sys.argv)
