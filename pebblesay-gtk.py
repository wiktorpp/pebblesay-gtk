import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import pebblesay

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def __getattr__(self, name):
        print(f'Handler "{name}" is not defined')
        return lambda self, *args: print(f'Handler "{name}" was called by a {self.get_name()}')

builder = Gtk.Builder()
builder.add_from_file("pebblesay-gtk.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()
Gtk.main()
