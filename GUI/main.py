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


class SupplyMenu(Screen):
    pass


class SupplyMedicine(Screen):
    pass


class CoviCare(App):
    def build(self):
        # setting the screen manager 
        sm = ScreenManager()
        # adding screens through widgets
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(SupplyMenu(name="supplymenu"))
        sm.add_widget(SupplyMedicine(name="supplymedicine"))
        return sm

#    def save_supplycity(self): 
#        supplycity = self.root.ids.supplycity.text
#        print(supplycity)

if __name__ == "__main__":
    CoviCare().run()
