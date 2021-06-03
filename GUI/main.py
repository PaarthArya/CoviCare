import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# setting the screens
class MainWindow(Screen):
    pass

class DonorMenu(Screen):
    pass

class CoviCare(App):
    def build(self):
        # setting the screen manager 
        sm = ScreenManager()
        # adding screens through widgets
        sm.add_widget(MainWindow(name = "main"))
        sm.add_widget(DonorMenu(name = "donormenu"))
        return sm

if __name__ == "__main__":
    CoviCare().run()
