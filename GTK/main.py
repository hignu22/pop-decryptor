#############################################################
#-------- this is version for gnome(gtk4, libadw) ---------##
# --------------version for cosmic(iced-rs)----------------## 
# --------in folder ../COSMIC-Rust/pop-decryptor-----------##
#############################################################

import sys
import os 

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    #functional code
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        #self.set_child(self.box1)

        # setting boxes
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now
        self.box1.append(self.box4) 
        self.box1.append(self.box5) 
        self.box1.append(self.box6) 
        self.box1.append(self.box7) 


        #size be default
        #self.set_default_size(600, 250)
        #self.set_title("PopDecryptor")

        #button for encrypt 
        self.button = Gtk.Button(label="Encrypt")
        self.button.connect('clicked', self.encrypt)
        self.box2.append(self.button) # Put button in the first of the two vertial boxes


        #id de disk


    def encrypt(self, button):
        ####  command for encrypt ####
        print(" GO !!! ")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="de.hignu22.pop_decrypt")
app.run(sys.argv)

####ende####