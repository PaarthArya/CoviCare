import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# creating the window elements for the application
# main grid comprises the subgrid for buttons
class MyGrid(Widget):
    pass

class CoviCare(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    CoviCare().run()
