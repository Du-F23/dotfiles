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

for x in autostart:
	os.system(x)
