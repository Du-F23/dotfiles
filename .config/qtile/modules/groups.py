# --==[ Groups ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keys import keys
from .settings import mod

# Workspaces
workspaces = {
    8: Group('   ', layout = 'max'),
    4: Group('   ', layout = 'monadtall'),
    2: Group('   ', layout = 'max', matches=[Match(wm_class=["firefox"])]),
    1: Group('   ', layout = 'monadtall'),
    3: Group('   ', layout = 'monadtall', matches=[Match(wm_class=["code"])]),
    0: Group(' 阮  ', layout = 'monadwide', matches=[Match(wm_class=["spotify"])]),
    9: Group(' 切  ', layout = 'monadtall', matches=[Match(wm_class=["telegram-desktop"])]),
}

groups = [
    workspaces[i] for i in workspaces
]

def get_key(name):
    return [
        k for k,
        g in workspaces.items()
        if g.name == name
    ][0]

# Navigation
for i in groups:
    keys.extend([
        # Switch to group {}
        Key([mod], str(get_key(i.name)), lazy.group[i.name].toscreen(), format(i.name)),

        # Move focused window to group {}
        Key([mod, 'shift'], str(get_key(i.name)), lazy.window.togroup(i.name), format(i.name)),
    ])
