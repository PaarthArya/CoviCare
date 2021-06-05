import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector


# open database connection and cursor
conn = mysql.connector.connect(host="localhost", user="root", password="Covicare123", database='covicare')
mycur = conn.cursor()


# global variables
city = ""


# setting the screens

#--------------------------------------SUPPLY SCREENS--------------------------------------------

class SupplyMenu(Screen):
    supplycity = ObjectProperty(None)

    def assigncity(self):
        global city
        city = self.city.text
        self.resetcity()

    def resetcity(self):
        self.city.text = ""


class SupplyMedicine(Screen):
    medid = ObjectProperty(None)
    medname = ObjectProperty(None)
    medaddress = ObjectProperty(None)
    medstock = ObjectProperty(None)
    medprice = ObjectProperty(None)
    medcontact = ObjectProperty(None)

    def assignmedicine(self):
        id = self.medid.text
        name = self.medname.text
        address = self.medaddress.text
        stock = self.medstock.text
        price = self.medprice.text
        contact = self.medcontact.text

        sql = "INSERT INTO MEDICINE VALUES(%s, %s, %s, %s, %s, %s, %s);"
        val = (id, name, city, address, stock, price, contact)
        # mycur.execute(sql, val)
        # conn.commit()

        self.resetmedicine()
        popupS()

    def resetmedicine(self):
        self.medid.text = ""
        self.medname.text = ""
        self.medaddress.text = ""
        self.medstock.text = ""
        self.medprice.text = ""
        self.medcontact.text = ""

#-------------------------------------ACCESS SCREENS--------------------------------------------

class AccessMenu(Screen):
    pass


class Navigation(Screen):
    pass


class MainWindow(Screen):
    pass


# global functions
def popupS():
    pop = Popup(title='Success', content=Label(text='Your entry has been recorded'), size_hint=(None, None), size=(300, 300))
    pop.open()


# main app build
class CoviCare(App):
    def build(self):
        # setting the screen manager 
        sm = ScreenManager()
        # adding screens through widgets
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(SupplyMenu(name="supplymenu"))
        sm.add_widget(SupplyMedicine(name="supplymedicine"))
        sm.add_widget(Navigation(name="navigation"))
        sm.add_widget(AccessMenu(name="accessmenu"))
        # returning the screen manager which provides the app
        return sm


# main program
if __name__ == "__main__":
    CoviCare().run()
    conn.close
