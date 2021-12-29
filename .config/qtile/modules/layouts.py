# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from .colors import color

# Layout config
config = {
    'border_normal': color[16],
    'border_focus': color[5],
    'border_width': 1,
    'single_border_width': 0,
    'margin': 7,
    'single_margin': 7,
}

layouts = [
    # layout.Max(),
    layout.MonadTall(**config),
    layout.MonadWide(**config),
]

# Floating windows
floating_layout = layout.Floating(
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class = 'confirmreset'),
        Match(wm_class = 'makebranch'),
        Match(wm_class = 'maketag'),
        Match(wm_class = 'ssh-askpass'),
        Match(title = 'branchdialog'),
        Match(title = 'pinentry'),
    ],
    border_normal = color[16],
    border_focus = color[5],
    border_width = 0,
)
