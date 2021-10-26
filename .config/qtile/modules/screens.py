# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

from .widgets import widgets

screens = [
    Screen(
        top=bar.Bar(
            # Import from widgets.py
            widgets,
            
            # Size
            15,

            # Margin
            margin=0,

            # Transparency
            opacity=1,
        ),
    ),
]
