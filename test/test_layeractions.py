# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import cocos
from cocos.director import director
from cocos.sprite import ActionSprite
from cocos.actions import *
import pyglet
        

if __name__ == "__main__":
    director.init()
    bg_layer = cocos.layer.ColorLayer(255,0,0,255)
    translate_layer = cocos.layer.Layer()
    x, y = director.get_window_size()
    translate_layer.add( bg_layer )
    translate_layer.do( MoveBy( (x/2, y/2), 5) )
    main_scene = cocos.scene.Scene (translate_layer)
    director.run (main_scene)