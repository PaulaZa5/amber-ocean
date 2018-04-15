import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from  kivy.graphics.vertex_instructions import Ellipse
kivy.require('1.9.1')

class AmberOceanLogin(Widget):
    pass

class AmberOceanUI(Widget):
    pass

class AmberOceanApp(App):
    def build(self):
        return AmberOceanUI()

if __name__ == '__main__':
    AmberOceanApp().run()
