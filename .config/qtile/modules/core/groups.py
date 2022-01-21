# --==[ Groups ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from ..utils.settings import mod
from .keys import keys

# Workspaces
main = [
    Group('1',
        label = '',
        layout = 'monadtall',
        matches = [
            Match(title = 'nvim')
        ]),

    Group('2',
        label = '',
        layout = 'stack',
        matches = [
            Match(wm_class = 'firefox'),
            Match(wm_class = 'chromium'),
        ]),

    Group('3',
        label = '',
        layout = 'monadtall',
        matches = [
            Match(wm_class = 'code'),
            Match(wm_class = 'vscodium'),
        ]),

    Group('4',
        label = '',
        layout = 'monadtall',
        matches = [
            Match(wm_class = 'thunar'),
            Match(title = 'ranger'),
        ]),

    Group('5',
        label = '',
        layout = 'stack',
        matches = [
            Match(wm_class = 'VirtualBox Manager')
        ]),

    Group('6',
        label = '',
        layout = 'stack',
        matches = [
            Match(title = 'GIMP Startup')
        ]),

    Group('7',
        label = '',
        layout = 'monadtall',
        matches = [
            Match(wm_class = 'evince'),
            Match(wm_class = 'libreoffice'),
        ]),

    Group('8',
        label = '',
        layout = 'monadtall',
        matches = [
            Match(wm_class = 'obs'),
            Match(wm_class = 'qBittorrent'),
        ]),

    Group('9',
        label = '',
        layout = 'stack',
        matches = [
            Match(wm_class = 'spotify'),
            Match(wm_class = 'Mplayer'),
            Match(wm_class = 'vlc'),
        ]),

    Group('0',
        label = '',
        layout = 'bsp',
        matches = [
            Match(wm_class = 'telegram-desktop'),
            Match(wm_class = 'discord'),
            Match(wm_class = 'caprine'),
            Match(title = 'WhatsApp Web'),
        ]),
]

groups = main

# Navigation
for i in groups:
    keys.extend([
        # Switch to group {}
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True)),

        # Move focused window to group {}
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])
