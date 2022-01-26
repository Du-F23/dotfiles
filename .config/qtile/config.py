# --==[ Qtile Config ]==--

# Import modules
from modules import *
from libqtile import hook

import os
import subprocess

@hook.subscribe.startup_once
def startup():
    subprocess.Popen(['.config/qtile/autostart.sh'])


# Config
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True
auto_minimize = False
wmname = 'qtile'
