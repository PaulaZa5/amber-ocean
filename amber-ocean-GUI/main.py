import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from  kivy.graphics.vertex_instructions import Ellipse
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

kivy.require('1.9.1')

			
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
