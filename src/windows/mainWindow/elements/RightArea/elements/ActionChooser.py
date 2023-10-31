"""
Author: Core447
Year: 2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This programm comes with ABSOLUTELY NO WARRANTY!

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
# Import gtk modules
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

# Import Python modules
from loguru import logger as log

class ActionChooser(Gtk.Box):
    def __init__(self, right_area, **kwargs):
        super().__init__(hexpand=True, vexpand=True, **kwargs)
        self.right_area = right_area

        self.build()

    def build(self):
        self.scrolled_window = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        self.append(self.scrolled_window)

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, hexpand=True, vexpand=True)
        self.scrolled_window.set_child(self.main_box)

        self.tmp_label = Gtk.Label(label="ActionChooser")
        self.main_box.append(self.tmp_label)

    def show(self, callback_function, *callback_args):
        self.callback_function = callback_function
        # Validate the callback function
        if not callable(self.callback_function):
            log.error(f"Invalid callback function: {self.callback_function}")
            return

        self.right_area.set_visible_child(self)