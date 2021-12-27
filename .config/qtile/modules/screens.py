# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

from .widgets import widgets

screens = [
    Screen(
        top = bar.Bar(
            # Source in widgets.py
            widgets,
            
            # Bar Size
            18,

            # Background Color
            background = "#00000000",

            # Margin
            margin = [7, 7, 0, 7],

            # Transparency
            opacity = 1,
        ),
    ),
]
