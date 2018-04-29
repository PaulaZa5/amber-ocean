import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.core.window import Window
import kivy
kivy.require('1.0.6')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import *
from kivy.graphics.vertex_instructions import Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,SlideTransition
from kivy.properties import ObjectProperty, StringProperty,NumericProperty
# from kivymd.navigationdrawer import NavigationDrawer
from kivy.uix.popup import *
from kivy.uix.label import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from personal_docks import PersonalDock
from amber import *
############## Login ##############
class Login(Widget):
     def submit_login(self):
        logname = self.login_name.text
        logpass = self.login_password.text
         # if logname == 'admin' and logpass == 'admin':
           #   return True
           
        for key, value in database.items():
            if is_personal_dock(key):
                if value.check_password(key,logpass):
                    return True
        else :
              popup = Popup(title='Test popup',
              content=Label(text='Wrong username or password'),
              size_hint=(None, None), size=self.size)
              popup.open()
              
class LoginScreen(Screen):
    pass

############## Registeration ##############
class Registeration(Widget):
     gender = StringProperty(None)
     def ismale(self):
          gender = "male"
          print (gender)
     def isfemale(self):
          gender = "female"
          print (gender)
     
     def registerAccount(self):
          print(self.name.text)
          #print(self.gender.text)
              
        #PersonalDock.RegisterAccount(self.name.text,self.gender.text,self.birthday.text,
                                     #self.password.text,self.email.text,self.phone_number.text)
class RegisterationScreen(Screen):
    pass

########### Forgetten Paswword ###########
class ForgetPassword(Widget):
    pass

class ForgetPasswordScreen(Screen):
    pass

########### Home ###########
class Home(Widget):
    pass
class HomeScreen(Screen):
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
