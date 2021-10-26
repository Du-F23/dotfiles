# --==[ Qtile Config ]==--

# noqa: F401
from typing import List

# Import modules
from modules.keys import keys
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.widgets import widget_defaults, extension_defaults
from modules.screens import screens
from modules.mouse import mouse
from modules.autostart import autostart

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
wmname = 'LG3D'
