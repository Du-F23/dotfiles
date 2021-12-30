# --==[ Autostart ]==--

import os

autostart = [
    # Keyboard layout
    'setxkbmap latam',

    # Compositor
    'picom &',

    # Screensaver
    'xset -dpms s off',
]

for i in autostart:
    os.system(i)
