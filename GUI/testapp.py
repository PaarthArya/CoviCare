from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Covicare123", database='covicare')
mycur = conn.cursor()
city = "New Delhi"

class RV(GridLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):

        mycur.execute("SELECT medicine_name, stock, price, contact FROM MEDICINE WHERE city = %s;", (city,))
        rows = mycur.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)



class TestApp(App):
    title = "Kivy RecycleView & SQLite3 Demo"

    def build(self):
        return RV()


if __name__ == "__main__":
    TestApp().run()