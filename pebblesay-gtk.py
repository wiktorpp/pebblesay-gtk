#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import pebblesay

class Handler:
    def __init__(self):
        pass

    def generate(self, *args):
        buffer = builder.get_object("textEntry").get_buffer()
        input = buffer.get_text(buffer.get_bounds().start, buffer.get_bounds().end, False)
        output = pebblesay.generate(input.split("\n"))
        textOutput = builder.get_object("textOutput")
        textOutput.set_text("\n".join(output))
        
    def copy(self, *args):
        text = builder.get_object("textOutput").get_text()
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(text, -1)

    def showAbout(self, button):
        about = builder.get_object("about")
        about.show_all()

    def onDestroy(self, window):
        Gtk.main_quit()

    def __getattr__(self, name):
        print(f'Handler "{name}" is not defined')
        return lambda self, *args: print(f'Handler "{name}" was called by a {self.get_name()}')

builder = Gtk.Builder()
try:
    builder.add_from_file("pebblesay-gtk.glade")
except:
    builder.add_from_file("/app/share/io.github.pebblesay/pebblesay-gtk.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()
Gtk.main()
