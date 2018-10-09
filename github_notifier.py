#!/usr/bin/env python3
import signal
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk, GObject
from notifier import Notifier
from indicator import Indicator
from threading import Thread
from menu import Menu


indicator = Indicator()
indicator.set_menu(Menu().get_inner())
notifier = Notifier(indicator)

thread = Thread(target=notifier.notify)
thread.setDaemon(True)
thread.start()

GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
