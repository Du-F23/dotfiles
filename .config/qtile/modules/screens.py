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
            20,

            # Background Color
            background = "#00000000",

            # Margin
            margin = [9, 20, 0, 20],

            # Transparency
            opacity = 1,
        ),
    ),
]
