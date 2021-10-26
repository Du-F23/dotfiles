# --==[ Key bindings ]==--

from libqtile.config import Key
from libqtile.lazy import lazy

from .settings import mod, terminal, browser, file_manager

keys = [
    # Switch between windows
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'space', lazy.layout.next()),

    # Move windows
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

    # Grow windows
    Key([mod, 'control'], 'h', lazy.layout.shrink()),
    Key([mod, 'control'], 'l', lazy.layout.grow()),

    # Toggle between layouts
    Key([mod], 'Tab', lazy.next_layout()),

    # Kill focused window
    Key([mod], 'w', lazy.window.kill()),

    # Restart Qtile
    Key([mod, 'control'], 'r', lazy.restart()),

    # Terminal
    Key([mod], 'Return', lazy.spawn(terminal)),

    # Menu
    Key([mod], 'm', lazy.spawn('rofi -show drun')),
    Key([mod, 'shift'], 'm', lazy.spawn('rofi -show')),

    # Browser
    Key([mod], 'b', lazy.spawn(browser)),

    # File Manager
    Key([mod], 'e', lazy.spawn(file_manager)),
    
    # Volume
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down +5%')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up +5%')),

    # Brightness
    Key([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
    Key([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

    # Player
    Key([mod], 'F9', lazy.spawn('playerctl --player=spotify previous')),
    Key([mod], 'F10', lazy.spawn('playerctl --player=spotify play-pause')),
    Key([mod], 'F11', lazy.spawn('playerctl --player=spotify next')),
]
