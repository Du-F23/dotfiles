# --==[ Groups ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keys import keys
from .settings import mod

# Workspaces
groups = [
    Group('1',
        label = ''),

    Group('2',
        label = ''),

    Group('3',
        label = ''),

    Group('4',
        label = ''),

    Group('5',
        label = ''),

    Group('6',
        label = ''),

    Group('7',
        label = ''),

    Group('8',
        label = ''),

    Group('9',
        label = ''),

    Group('0',
        label = ''),
]

# Navigation
for i in groups:
    keys.extend([
        # Switch to group {}
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True)),

        # Move focused window to group {}
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])


