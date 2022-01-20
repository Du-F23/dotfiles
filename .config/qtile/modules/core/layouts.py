# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from .colors import color

# Layout config
def config(layout_name):
    config = {
        'border_normal': color[8],
        'border_focus': color[5],
        'border_width': 1,
        'single_border_width': 0,
        'margin': 9,
        'single_margin': 9,
    }
    if layout_name == 'bsp':
        config['fair'] = False
        config['grow_amount'] = 3
        config['lower_right'] = False

    elif layout_name == 'xmonad':
        config['min_ratio'] = 0.30
        config['max_ratio'] = 0.70
        config['change_ratio'] = 0.02

    elif layout_name == 'stack':
        config['border_width'] = 0
        config['num_stacks'] = 1
    return config

layouts = [
    # layout.Max(),
    layout.Bsp(**config('bsp')),
    layout.MonadTall(**config('xmonad')),
    layout.MonadWide(**config('xmonad')),
    layout.Stack(**config('stack')),
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
    border_normal = color[8],
    border_focus = color[7],
    border_width = 1,
)
