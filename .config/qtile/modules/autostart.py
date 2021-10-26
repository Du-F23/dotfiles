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
]

for x in autostart:
	os.system(x)
