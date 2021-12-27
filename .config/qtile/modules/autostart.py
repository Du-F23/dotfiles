# --==[ Autostart ]==--

import os
from .settings import wallpaper

autostart = [
    # Keyboard layout
    'setxkbmap latam',

    # Wallpaper
    'feh --bg-fill ' + wallpaper,

    # Compositor
    'picom &',

    # Screensaver
    'xset -dpms s off',
]

for i in autostart:
    os.system(i)
