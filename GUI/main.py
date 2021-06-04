import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector


# open database connection
conn = mysql.connector.connect(host="localhost", user="root", password="Covicare123", database='covicare')

# prepare a cursor object using cursor() method
mycur = conn.cursor()


# global variables
city = ""


# setting the screens
class SupplyMenu(Screen):
    supplycity = ObjectProperty(None)

    def assigncity(self):
        global city
        city = self.city.text

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
        mycur.execute(sql, val)
        conn.commit()
     
    def resetmedicine(self):
        self.medid.text = ""
        self.medname.text = ""
        self.medaddress.text = ""
        self.medstock.text = ""
        self.medprice.text = ""
        self.medcontact.text = ""


class MainWindow(Screen):
    pass


# DEFINE ALL GLOBAL FUNCTIONS



# ---------------------------

class CoviCare(App):
    def build(self):
        # setting the screen manager 
        sm = ScreenManager()
        # adding screens through widgets
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(SupplyMenu(name="supplymenu"))
        sm.add_widget(SupplyMedicine(name="supplymedicine"))
        return sm

    def supplyCity(self): 
        x = self.root.ids.supplycity.text
        print(x)


if __name__ == "__main__":
    CoviCare().run()
    conn.close
