# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from .colorscheme import hex

# Layout config
properties = {
    'border_normal': hex['normal'],
    'border_focus': hex['border'],
    'border_width': 1,
    'single_border_width': 0,
    'margin': 5,
    'single_margin': 5,
}

layouts = [
    layout.Max(),   
    layout.MonadTall(
        **properties
    ),
    layout.MonadWide(
        **properties
    ),
]

# Floating windows
floating_layout = layout.Floating(
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_normal=hex['normal'],
    border_focus=hex['border'],
    border_width=0,
)
