#############################################################
#-------- this is version for gnome(gtk4, libadw) ---------##
# --------------version for cosmic(iced-rs)----------------## 
# --------in folder ../COSMIC-Rust/pop-decryptor-----------##
#############################################################

import sys
import os 
import subprocess

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk

#adding style.css
css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

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
        
        self.box2.set_css_classes(['pxs'])


        self.header = Gtk.HeaderBar()
        self.header.set_css_classes(['header'])
        self.set_titlebar(self.header)
        self.open_button = Gtk.Button(label="Info")
        self.new_file    = Gtk.Button(label="New")
        self.open_button.set_css_classes(['drei'])
        self.new_file.set_css_classes   (['drei'])
        self.header.pack_start(self.open_button)
        self.header.pack_start(self.new_file)

        self.open_button.connect('clicked', self.show_about)
        self.new_file.connect('clicked', self.info_func)


        #password de disk
        self.label_pass = Gtk.Label(label = "new password for disk ( also root ! )")
        self.box2.append(self.label_pass)
        self.label_pass.set_css_classes(['size_all'])
        self.input_line = Gtk.PasswordEntry()
        self.box2.append(self.input_line)
        self.input_line.set_css_classes(['zwo'])
        #size be default
        #self.set_default_size(600, 250)
        self.set_title("PopDecryptor")

        #id de disk
        self.check = Gtk.CheckButton(label="add sdb")
        self.check1 = Gtk.CheckButton(label="add sda")
        self.check2 = Gtk.CheckButton(label="add sdc")
        self.box2.append(self.check)
        self.box2.append(self.check1)
        self.box2.append(self.check2)


        #button for encrypt 
        self.button = Gtk.Button(label="Encrypt")
        self.button.connect('clicked', self.encrypt)
        self.box2.append(self.button) # Put button in the first of the two vertial boxes
        self.button.set_css_classes(['ein'])
        self.button.set_css_classes(['size_all'])


        ########-Dialog-Window-########
        self.window_dialog = Gtk.Dialog()

    def encrypt(self, button):
        ####  command for encrypt ####
        print(" GO !!! ")
        if self.check.get_active() :
            print("check")
            procs = subprocess.Popen(["cryptsetup luksAddKey /dev/sda3"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            os.write(procs.stdin.fileno(), self.input_line.encode())

        elif self.check1.get_active() :
            print("check")
            procs = subprocess.Popen(["cryptsetup luksAddKey /dev/sdb"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            os.write(procs.stdin.fileno(), self.input_line.encode())
        elif self.check1.get_active() :
            print("check")
            procs = subprocess.Popen(["cryptsetup luksAddKey /dev/sdc"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            os.write(procs.stdin.fileno(), self.input_line.encode())
        else :
            print(" --- ERROR 404 :( ")


    def info_func(self, open_button):
        os.system('python3 info_win.py')
    
    def show_about(self, open_button ):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self) 
        self.about.set_modal(self)  
        self.about.set_authors(["HiGnu22"])
        self.about.set_copyright("Copyright 2023 hignu22")
        self.about.set_license_type(Gtk.License.GPL_2_0)
        self.about.set_website("http://github.com/hignu22/pop-decryptor")
        self.about.set_website_label("GitHub by PopDecryptor")
        self.about.set_version("1.0 alfa")
        self.about.set_logo_icon_name()
        self.about.show()
        #self.about.set_css_classes(['about_css'])

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