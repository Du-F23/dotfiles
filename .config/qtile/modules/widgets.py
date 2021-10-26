# --==[ Widgets ]==--

from libqtile import widget

from .colorscheme import hex
from .settings import font, fontsize, interface, backlight

# General bar settings
widget_defaults = dict(
    font=font,
    fontsize=fontsize,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Functions
def base(bg, txt):
    return {
        'background': bg,
        'foreground': txt,
    }

def triangle(icon):
    return {
        'fontsize': 24,
        'padding': -2,
        'text': icon,
    }

def left(bg, txt):
    return widget.TextBox(
        **base(bg, txt),
        **triangle(''),
    )

def right(bg, txt):
    return widget.TextBox(
        **base(bg, txt),
        **triangle(''),
    )

def icon(bg, txt, icon):
    return widget.TextBox(
        **base(bg, txt),
        fontsize=12,
        padding=3,
        text=icon,
    )

# Widgets
def distro(bg, txt):
    return [
        widget.TextBox(
            **base(bg, txt),
            text="  ",
            fontsize=12,
        ),
    ]

def net(bg, txt):
    return [
        widget.Wlan(
            **base(bg, txt),
            interface=interface,
            format='Net:',
            disconnected_message='Error',
        ),
        widget.Net(
            **base(bg, txt),
            interface=interface,
            use_bits=True,
            format='{down} ↓↑{up}',
        ),
        icon(bg, txt, ' '),
    ]

def layout(bg, txt):
    return [
        widget.CurrentLayout(
            **base(bg, txt),
        ),
        icon(bg, txt, ' ﬿'),
    ]

def memory(bg, txt):
    return [
        widget.Memory(
            **base(bg, txt),
            format='{MemUsed: .0f}{mm}',
        ),
        icon(bg, txt, '﬙ '),
    ]

def cpu(bg, txt):
    return [
        widget.CPU(
            **base(bg, txt),
            format='{load_percent}%',
        ),
        icon(bg, txt, ' '),
    ]

def groups(bg):
    return [
        widget.Spacer(background=bg),
        widget.GroupBox(
            highlight_method='block',
            fontsize=14,
            margin_x=0,
            padding_x=-1,
            rounded=False,
            disable_drag=True,
            use_mouse_wheel=False,
            background=bg,
            active=hex['active'],
            inactive=hex['inactive'],
            this_screen_border=hex['focus'],
            this_current_screen_border=hex['focus'],
        ),
        widget.Spacer(background=bg),
    ]

def volume(bg, txt):
    return [
        icon(bg, txt, ' '),
        widget.PulseVolume(
            **base(bg, txt),
            limit_max_volume=True,
        ),
    ]

def brightness(bg, txt):
    return [
        icon(bg, txt, ' '),
        widget.Backlight(
            **base(bg, txt),
            backlight_name=backlight,
        ),
    ]

def harddisk(bg, txt):
    return [
        icon(bg, txt, ' '),
        widget.DF(
            **base(bg, txt),
            visible_on_warn=False,
            format='Usage: {r:.2f}%',
        ),
    ]

def clock(bg, txt):
    return [
        icon(bg, txt, ' '),
        widget.Clock(
            **base(bg, txt),
            format='%H:%M - %A, %b %-d',
        ),
    ]

def close(bg, txt):
    return [
        widget.QuickExit(
            **base(bg, txt),
            countdown_format='{}  ',
            countdown_start=5,
            default_text='襤  ',
            fontsize=12,
        ),
    ]

widgets = [
    # Base 1
    *distro(hex['base1'], hex['text']),
    left(hex['base2'], hex['base1']),

    # Base 2
    *net(hex['base2'], hex['color1']),
    left(hex['base3'], hex['base2']),

    # Base 3
    *layout(hex['base3'], hex['color2']),
    left(hex['base4'], hex['base3']),

    # Base 4
    *memory(hex['base4'], hex['color3']),
    left(hex['base5'], hex['base4']),

    # Base 5
    *cpu(hex['base5'], hex['color4']),
    left(hex['center'], hex['base5']),

    # Center
    *groups(hex['center']),

    # Base 5
    right(hex['center'], hex['base5']),
    *volume(hex['base5'], hex['color4']),

    # Base 4
    right(hex['base5'], hex['base4']),
    *brightness(hex['base4'], hex['color3']),

    # Base 3
    right(hex['base4'], hex['base3']),
    *harddisk(hex['base3'], hex['color2']),

    # Base 2
    right(hex['base3'], hex['base2']),
    *clock(hex['base2'], hex['color1']),

    # Base 1
    right(hex['base2'], hex['base1']),
    *close(hex['base1'], hex['text']),
]
