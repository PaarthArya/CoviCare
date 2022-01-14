import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector

# open database connection and cursor
conn = mysql.connector.connect(host="localhost", user="root", password="Covicare123", database='covicare')
mycur = conn.cursor()

city = ""

# setting the screens

# --------------------------------------SUPPLY SCREENS--------------------------------------------

class SupplyMenu(Screen):
    supplycity = ObjectProperty(None)

    # store city input in global variable for data entry and change screens
    def assigncitym(self):
        global city

        if self.supplycity.text != "":
            city = self.supplycity.text
            sm.current = "supplymedicine"
        else:
            invalidcity()

        self.resetcity()

    def assigncitybe(self):
        global city

        if self.supplycity.text != "":
            city = self.supplycity.text
            sm.current = "supplybed"
        else:
            invalidcity()

        self.resetcity()

    def assigncitye(self):
        global city

        if self.supplycity.text != "":
            city = self.supplycity.text
            sm.current = "supplyequipment"
        else:
            invalidcity()

        self.resetcity()

    def assigncitybl(self):
        global city

        if self.supplycity.text != "":
            city = self.supplycity.text
            sm.current = "supplyblood"
        else:
            invalidcity()

        self.resetcity()

    def resetcity(self):
        self.supplycity.text = ""


class SupplyMedicine(Screen):
    # retrieve inputs in local variables
    medid = ObjectProperty(None)
    medname = ObjectProperty(None)
    medaddress = ObjectProperty(None)
    medstock = ObjectProperty(None)
    medprice = ObjectProperty(None)
    medcontact = ObjectProperty(None)

    # insert into database and display popup
    def assignmedicine(self):
        id = self.medid.text
        name = self.medname.text
        address = self.medaddress.text
        stock = self.medstock.text
        price = self.medprice.text
        contact = self.medcontact.text

        if str(id).isdigit() and name != "" and address != "" and str(stock).isdigit() and (
                str(price).isdigit() or str(price).isdecimal()) and contact != "":
            sql = "INSERT INTO MEDICINE VALUES(%s, %s, %s, %s, %s, %s, %s);"
            val = (id, name, city, address, stock, price, contact)
            mycur.execute(sql, val)
            conn.commit()
            sm.current = "navigation"
            popupS()
        else:
            invalid()

        self.resetmedicine()

    # reset inputs
    def resetmedicine(self):
        self.medid.text = ""
        self.medname.text = ""
        self.medaddress.text = ""
        self.medstock.text = ""
        self.medprice.text = ""
        self.medcontact.text = ""


class SupplyBed(Screen):
    hospid = ObjectProperty(None)
    hospname = ObjectProperty(None)
    hospaddress = ObjectProperty(None)
    bedtype = ObjectProperty(None)
    bedcount = ObjectProperty(None)
    hospcontact = ObjectProperty(None)

    def assignbed(self):
        id = self.hospid.text
        name = self.hospname.text
        address = self.hospaddress.text
        htype = self.bedtype.text
        count = self.bedcount.text
        contact = self.hospcontact.text

        if str(id).isdigit() and name != "" and address != "" and htype != "" and str(
                count).isdigit() and contact != "":
            sql = "INSERT INTO BED VALUES(%s, %s, %s, %s, %s, %s, %s);"
            val = (id, name, city, address, htype, count, contact)
            mycur.execute(sql, val)
            conn.commit()
            sm.current = "navigation"
            popupS()
        else:
            invalid()

        self.resetbed()

    def resetbed(self):
        self.hospid.text = ""
        self.hospname.text = ""
        self.hospaddress.text = ""
        self.bedtype.text = ""
        self.bedcount.text = ""
        self.hospcontact.text = ""


class SupplyEquipment(Screen):
    equipid = ObjectProperty(None)
    equiptype = ObjectProperty(None)
    equipstock = ObjectProperty(None)
    equipprice = ObjectProperty(None)
    equipcontact = ObjectProperty(None)

    def assignequip(self):
        id = self.equipid.text
        etype = self.equiptype.text
        stock = self.equipstock.text
        price = self.equipprice.text
        contact = self.equipcontact.text

        if str(id).isdigit() and etype != "" and str(stock).isdigit() and (
                str(price).isdigit() or str(price).isdecimal()) and contact != "":
            sql = "INSERT INTO EQUIPMENT VALUES(%s, %s, %s, %s, %s, %s);"
            val = (id, etype, city, stock, price, contact)
            mycur.execute(sql, val)
            conn.commit()
            sm.current = "navigation"
            popupS()
        else:
            invalid()

        self.resetequip()

    def resetequip(self):
        self.equipid.text = ""
        self.equiptype.text = ""
        self.equipstock.text = ""
        self.equipprice.text = ""
        self.equipcontact.text = ""


class SupplyBlood(Screen):
    bloodid = ObjectProperty(None)
    bloodname = ObjectProperty(None)
    bloodtype = ObjectProperty(None)
    bloodcontact = ObjectProperty(None)

    def assignblood(self):
        id = self.bloodid.text
        name = self.bloodname.text
        btype = self.bloodtype.text
        contact = self.bloodcontact.text

        if str(id).isdigit() and name != "" and btype != "" and contact != "":
            sql = "INSERT INTO BLOOD VALUES(%s, %s, %s, %s, %s);"
            val = (id, name, city, btype, contact)
            mycur.execute(sql, val)
            conn.commit()
            sm.current = "navigation"
            popupS()
        else:
            invalid()

        self.resetblood()

    def resetblood(self):
        self.bloodid.text = ""
        self.bloodname.text = ""
        self.bloodtype.text = ""
        self.bloodcontact.text = ""


# -------------------------------------ACCESS SCREENS--------------------------------------------


class AccessMenu(Screen):
    accesscity = ObjectProperty(None)

    # store city input in global variable for data entry and change screens
    def assigncitym(self):
        global city

        if self.accesscity.text != "":
            city = self.accesscity.text
            mycur.execute("SELECT medicine_name, stock, price, contact FROM MEDICINE WHERE city = %s;", (city,))
            rows = mycur.fetchall()
            if rows == []:
                citynotfound()
            else:
                sm.current = "blank"
                CoviCare().stop()
                MedicineDisplay().run()
        else:
            invalidcity()
        
        self.resetcity()

    def assigncitybe(self):
        global city

        if self.accesscity.text != "":
            city = self.accesscity.text
            mycur.execute("SELECT hospital_name, type_of_bed, no_of_beds, contact FROM BED WHERE city = %s;", (city,))
            rows = mycur.fetchall()
            if rows == []:
                citynotfound()
            else:
                sm.current = "blank"
                CoviCare().stop()
                BedDisplay().run()
        else:
            invalidcity()

        self.resetcity()

    def assigncitye(self):
        global city

        if self.accesscity.text != "":
            city = self.accesscity.text
            mycur.execute("SELECT equipment_type, stock, price, contact FROM EQUIPMENT WHERE city = %s;", (city,))
            rows = mycur.fetchall()
            if rows == []:
                citynotfound()
            else:
                sm.current = "blank"
                CoviCare().stop()
                EquipmentDisplay().run()
        else:
            invalidcity()

        self.resetcity()

    def assigncitybl(self):
        global city

        if self.accesscity.text != "":
            city = self.accesscity.text
            mycur.execute("SELECT donor_name, blood_type, contact FROM BLOOD WHERE city = %s;", (city,))
            rows = mycur.fetchall()
            if rows == []:
                citynotfound()
            else:
                sm.current = "blank"
                CoviCare().stop()
                BloodDisplay().run()
        else:
            invalidcity()

        self.resetcity()

    def resetcity(self):
        self.accesscity.text = ""


class AccessMedicine(GridLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(AccessMedicine, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):

        mycur.execute("SELECT medicine_name, stock, price, contact FROM MEDICINE WHERE city = %s;", (city,))
        rows = mycur.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)

    def changeapps(self):
        MedicineDisplay().stop()

class MedicineDisplay(App):
    title = "Medicine Access"

    def build(self):
        return AccessMedicine()


class AccessBed(GridLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(AccessBed, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):

        mycur.execute("SELECT hospital_name, type_of_bed, no_of_beds, contact FROM BED WHERE city = %s;", (city,))
        rows = mycur.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)

    def changeapps(self):
        BedDisplay().stop()

class BedDisplay(App):
    title = "Bed Access"

    def build(self):
        return AccessBed()


class AccessEquipment(GridLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(AccessEquipment, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):

        mycur.execute("SELECT equipment_type, stock, price, contact FROM EQUIPMENT WHERE city = %s;", (city,))
        rows = mycur.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)

    def changeapps(self):
        EquipmentDisplay().stop()

class EquipmentDisplay(App):
    title = "Equipment Access"

    def build(self):
        return AccessEquipment()


class AccessBlood(GridLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(AccessBlood, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):

        mycur.execute("SELECT donor_name, blood_type, contact FROM BLOOD WHERE city = %s;", (city,))
        rows = mycur.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)

    def changeapps(self):
        BloodDisplay().stop()

class BloodDisplay(App):
    title = "Blood Access"

    def build(self):
        return AccessBlood()


class Navigation(Screen):
    pass


class Blank(Screen):
    pass


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# global functions
def popupS():
    pop = Popup(title='Success', content=Label(text='Your entry has been recorded.', font_size=15),
                size_hint=(None, None), size=(300, 300))
    pop.open()


def invalid():
    pop = Popup(title='Error', content=Label(text='Invalid Entry! Please try again.', font_size=15),
                size_hint=(None, None), size=(300, 300))
    pop.open()


def invalidcity():
    pop = Popup(title='Error', content=Label(text='City field cannot be empty.', font_size=15), size_hint=(None, None),
                size=(300, 300))
    pop.open()


def citynotfound():
    pop = Popup(title='Error', content=Label(text='Sorry! No leads found in this city.', font_size=15), size_hint=(None, None),
                size=(300, 300))
    pop.open()


# build using kv file
kv = Builder.load_file("covicare.kv")

# setting the screen manager
sm = WindowManager()

# adding screens through widgets
sm.add_widget(MainWindow(name="main"))
sm.add_widget(Navigation(name="navigation"))

# supply
sm.add_widget(SupplyMenu(name="supplymenu"))
sm.add_widget(SupplyMedicine(name="supplymedicine"))
sm.add_widget(SupplyBed(name="supplybed"))
sm.add_widget(SupplyEquipment(name="supplyequipment"))
sm.add_widget(SupplyBlood(name="supplyblood"))

# access        
sm.add_widget(AccessMenu(name="accessmenu"))
sm.add_widget(Blank(name = "blank"))

# current screen
sm.current = "main"


# main app build
class CoviCare(App):
    def build(self):
        # returning the screen manager which provides the app
        return sm


# main program
if __name__ == "__main__":
        CoviCare().run()
