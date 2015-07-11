#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgkeyboard"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgkeyboard.cpp'

# OpenSceneGraph example, osgkeyboard.
#*
#*  Permission is hereby granted, free of charge, to any person obtaining a copy
#*  of this software and associated documentation files (the "Software"), to deal
#*  in the Software without restriction, including without limitation the rights
#*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#*  copies of the Software, and to permit persons to whom the Software is
#*  furnished to do so, subject to the following conditions:
#*
#*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#*  THE SOFTWARE.
#

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osg/io_utils>

#include <osg/MatrixTransform>
#include <osg/Geode>
#include <osg/Group>
#include <osg/Switch>
#include <osg/Notify>
#include <osg/Geometry>

#include <osgText/Text>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>


class KeyboardModel (osg.Referenced) :

        KeyboardModel()  createKeyboard() 
        
        def getScene():
        
             return _scene.get() 
        
        keyChange = void(int key, int virtualKey, int value)
        
        ~KeyboardModel() 

        addKey = osg.Switch*(osg.Vec3 pos, int key, str text,float width, float height)

        createKeyboard = void()

        typedef std.map<int, osg.Switch > KeyModelMap
        
        _scene = osg.Group()
        _keyModelMap = KeyModelMap()
        _inputText = osgText.Text()



void KeyboardModel.keyChange(int key, int virtualKey, int value)
    osg.notify(osg.INFO), "key value change, code=", std.hex, key, "\t value=", value, std.dec

    # toggle the keys graphical representation on or off via osg.Swithc
    itr = _keyModelMap.find(virtualKey)
    if itr!=_keyModelMap.end() :
        itr.second.setSingleChildOn(value)
    
    if value :
        # when a key is pressed add the data to the text field
        
        if key>0  key<256 :
            # just add ascii characters right now...
            _inputText.getText().push_back(key)
            _inputText.update()
        elif key==osgGA.GUIEventAdapter.KEY_Return :
            _inputText.getText().push_back('\n')
            _inputText.update()
        elif key==osgGA.GUIEventAdapter.KEY_BackSpace || key==osgGA.GUIEventAdapter.KEY_Delete : 
            if !_inputText.getText().empty() :
                _inputText.getText().pop_back()
                _inputText.update()
        
    

osg.Switch* KeyboardModel.addKey(osg.Vec3 pos, int key, str text,float width, float height)

    geodeUp = osg.Geode()
        textUp = osgText.Text()
        textUp.setFont("fonts/arial.ttf")
        textUp.setColor(osg.Vec4(1.0,1.0,1.0,1.0))
        textUp.setCharacterSize(height)
        textUp.setPosition(pos)
        textUp.setDrawMode(osgText.Text.TEXT#|osgText.Text.BOUNDINGBOX)
        textUp.setAlignment(osgText.Text.LEFT_CENTER)
        textUp.setAxisAlignment(osgText.Text.XZ_PLANE)
        textUp.setText(text)
        
        geodeUp.addDrawable(textUp)
    
    geodeDown = osg.Geode()
        textDown = osgText.Text()
        textDown.setFont("fonts/arial.ttf")
        textDown.setColor(osg.Vec4(1.0,0.0,1.0,1.0))
        textDown.setCharacterSize(height)
        textDown.setPosition(pos)
        textDown.setDrawMode(osgText.Text.TEXT#||osgText.Text.BOUNDINGBOX)
        textDown.setAlignment(osgText.Text.LEFT_CENTER)
        textDown.setAxisAlignment(osgText.Text.XZ_PLANE)
        textDown.setText(text)
        
        geodeDown.addDrawable(textDown)

    model = osg.Switch()
    model.addChild(geodeUp,True)
    model.addChild(geodeDown,False)
    
    _scene.addChild(model)

    _keyModelMap[key] = model
    
    pos.x() += width
    
    return model
    

void KeyboardModel.createKeyboard()
    _scene = osg.Group()
    
    origin = osg.Vec3(0.0,0.0,0.0)
    pos = origin
    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Control_L,"Ctrl",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Super_L,"Super",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Alt_L,"Alt",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Space,"Space",3.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Mode_switch,"Switch",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Super_R,"Super",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Menu,"Menu",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Control_R,"Ctrl",2.0,0.5)

    middle = osg.Vec3(pos.x()+1.0,0.0,0.0)
    
    pos.x() = 0.0
    pos.z() += 1.0

    addKey(pos,osgGA.GUIEventAdapter.KEY_Shift_L,"Shift",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Backslash,"\\",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Z,"Z",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_X,"X",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_C,"C",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_V,"V",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_B,"B",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_N,"N",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_M,"M",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Comma,",",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Period,".",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Slash,"/",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Shift_R,"Shift",2.0,0.5)

    pos.x() = 0.0
    pos.z() += 1.0
    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Caps_Lock,"Caps",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_A,"A",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_S,"S",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_D,"D",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F,"F",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_G,"G",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_H,"H",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_J,"J",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_K,"K",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_L,"L",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Semicolon,"",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Quote,"'",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Hash,"#",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Return,"Return",4.0,0.5)

    pos.x() = 0.0
    pos.z() += 1.0
    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Tab,"Tab",2.0,0.5)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Q,"Q",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_W,"W",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_E,"E",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_R,"R",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_T,"T",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Y,"Y",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_U,"U",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_I,"I",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_O,"O",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_P,"P",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Leftbracket,"[",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Rightbracket,"]",1.0,1.0)

    pos.x() = 0.0
    pos.z() += 1.0
    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Backquote,"`",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_1,"1",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_2,"2",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_3,"3",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_4,"4",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_5,"5",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_6,"6",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_7,"7",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_8,"8",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_9,"9",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_0,"0",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Minus,"-",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Equals,"=",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_BackSpace,"Backspace",3.0,0.5)

    pos.x() = 0.0
    pos.z() += 1.5
    
    F_height = 0.5
    addKey(pos,osgGA.GUIEventAdapter.KEY_Escape,"Esc",2.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F1,"F1",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F2,"F2",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F3,"F3",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F4,"F4",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F5,"F5",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F6,"F6",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F7,"F7",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F8,"F8",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F9,"F9",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F10,"F10",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F11,"F11",1.0,F_height)
    addKey(pos,osgGA.GUIEventAdapter.KEY_F12,"F12",1.0,F_height)


    
    cursorMoveHeight = 0.35

    pos = middle    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Left,"Left",1.0,cursorMoveHeight)
    down = pos
    addKey(pos,osgGA.GUIEventAdapter.KEY_Down,"Down",1.0,cursorMoveHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Right,"Right",1.0,cursorMoveHeight)
    
    keypad = pos
    keypad.x()+=1.0

    pos = down
    pos.z() += 1.0
    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Up,"Up",1.0,cursorMoveHeight)
    

    homeHeight = 0.35
    pos = middle
    pos.z() += 3.0    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Delete,"Delete",1.0,homeHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_End,"End",1.0,homeHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Page_Down,"Page\nDown",1.0,homeHeight)
    
    pos = middle
    pos.z() += 4.0    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Insert,"Insert",1.0,homeHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Home,"Home",1.0,homeHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Page_Up,"Page\nUp",1.0,homeHeight)

    pos = middle
    pos.z() += 5.5    
    addKey(pos,osgGA.GUIEventAdapter.KEY_Print,"PrtScrn\nSysRq",1.0,homeHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Scroll_Lock,"ScrLk",1.0,homeHeight)
    addKey(pos,osgGA.GUIEventAdapter.KEY_Pause,"Pause\nBreak",1.0,homeHeight)
    
    

    pos = keypad
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Insert,"0",2.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Delete,".",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Enter,"Enter",1.0,homeHeight)
    
    pos = keypad
    pos.z() += 1.0
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_End,"1",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Down,"2",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Page_Down,"3",1.0,1.0)

    pos = keypad
    pos.z() += 2.0
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Left,"4",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Begin,"5",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Right,"6",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Add,"+",1.0,1.0)

    pos = keypad
    pos.z() += 3.0
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Home,"7",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Up,"8",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Page_Up,"9",1.0,1.0)

    pos = keypad
    pos.z() += 4.0
    addKey(pos,osgGA.GUIEventAdapter.KEY_Num_Lock,"Num\nLock",1.0,0.3)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Divide,"/",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Multiply,"*",1.0,1.0)
    addKey(pos,osgGA.GUIEventAdapter.KEY_KP_Subtract,"-",1.0,1.0)
    
    totalWidth = pos.x()-origin.x()
    pos = origin
    pos.z() += -1.5

    geodeInput = osg.Geode()
        _inputText = osgText.Text()
        _inputText.setFont("fonts/arial.ttf")
        _inputText.setColor(osg.Vec4(1.0,1.0,0.0,1.0))
        _inputText.setCharacterSize(1.0)
        _inputText.setMaximumWidth(totalWidth)
        _inputText.setPosition(pos)
        _inputText.setDrawMode(osgText.Text.TEXT#||osgText.Text.BOUNDINGBOX)
        _inputText.setAlignment(osgText.Text.BASE_LINE)
        _inputText.setAxisAlignment(osgText.Text.XZ_PLANE)
        _inputText.setDataVariance(osg.Object.DYNAMIC)
        _inputText.setText("Press some keys...")
        
        geodeInput.addDrawable(_inputText.get())
        
        _scene.addChild(geodeInput)







class KeyboardEventHandler (osgGA.GUIEventHandler) :
    
        KeyboardEventHandler(KeyboardModel* keyboardModel):
            _keyboardModel(keyboardModel) 
    
        virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)

#if 1

#            osg.notify(osg.NOTICE), "Mouse ", ea.getButtonMask()

            #define PRINT(mask) osg.notify(osg.NOTICE), #mask, " =", (ea.getModKeyMask()  mask)
            switch(ea.getEventType())
                case(osgGA.GUIEventAdapter.KEYDOWN):
                case(osgGA.GUIEventAdapter.KEYUP):
                    osg.notify(osg.NOTICE)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_LEFT_SHIFT)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_RIGHT_SHIFT)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_LEFT_ALT)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_RIGHT_ALT)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_LEFT_CTRL)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_RIGHT_CTRL)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_LEFT_META)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_RIGHT_META)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_LEFT_SUPER)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_RIGHT_SUPER)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_LEFT_HYPER)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_RIGHT_HYPER)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_NUM_LOCK)
                    PRINT(osgGA.GUIEventAdapter.MODKEY_CAPS_LOCK)
                    break
                default:
                    break
#endif
            switch(ea.getEventType())
                case(osgGA.GUIEventAdapter.KEYDOWN):
                    _keyboardModel.keyChange(ea.getKey(), ea.getUnmodifiedKey(),1)
                    return True
                case(osgGA.GUIEventAdapter.KEYUP):
                    _keyboardModel.keyChange(ea.getKey(), ea.getUnmodifiedKey(),0)
                    return True

                default:
                    return False
        
        _keyboardModel = KeyboardModel()
        


int main(int , char **)
    viewer = osgViewer.Viewer()

    keyboardModel = KeyboardModel()

    viewer.addEventHandler(osgViewer.StatsHandler)()
    viewer.addEventHandler(osgViewer.WindowSizeHandler())
    viewer.addEventHandler(KeyboardEventHandler(keyboardModel.get()))
    viewer.setSceneData( keyboardModel.getScene() )

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
