import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.core.window import Window
import kivy
kivy.require('1.0.6')
from kivy.core.window import Window
from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
# FIXME this shouldn't be necessary
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from  kivy.graphics.vertex_instructions import Ellipse
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



			
########### Login ###########
class Login(Widget):
    pass

class LoginScreen(Screen):
    pass

########### Registeration ###########
class Registeration(Widget):
    pass

class RegisterationScreen(Screen):
    pass

########### Forgetten Paswword ###########
class ForgetPassword(Widget):
    pass

class ForgetPasswordScreen(Screen):
    pass

########### Screen Manager ###########
class ScreenManagement(ScreenManager):
    pass

########### Load .kv File ###########
AmberOcean = Builder.load_file("amberocean.kv")

########### Build Class ###########
class AmberOceanApp(App):
    def build(self):
        return AmberOcean

########### Run Build ###########
if __name__ == '__main__':
    AmberOceanApp().run()
