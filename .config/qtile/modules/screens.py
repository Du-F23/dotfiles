# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

from .widgets import widgets

screens = [
    Screen(
        top=bar.Bar(
            # Source in widgets.py
            widgets,
            
            # Size
            20,

            # Margin
            margin=0,

            # Transparency
            opacity=0.8,
        ),
    ),
]
