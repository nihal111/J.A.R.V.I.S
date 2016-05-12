from gi.repository import Gio
import glob
from random import randint
import os 


directory = os.path.dirname(os.path.realpath(__file__))
wallpapers = glob.glob("wallpapers/*")
x = randint(0,len(wallpapers)-1)

SCHEMA = 'org.gnome.desktop.background'
KEY = 'picture-uri'
gsettings = Gio.Settings.new(SCHEMA)
background = directory+"/" + wallpapers[x]
gsettings.set_string(KEY, "file://" + background)