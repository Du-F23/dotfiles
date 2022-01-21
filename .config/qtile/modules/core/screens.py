# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

from ..utils.settings import wallpaper
from ..extras.widgets import widgets, widgets_tmp

screens = [
    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        top = bar.Bar(
            # Source in widgets.py
            widgets,

            # Bar Size
            20,

            # Background Color
            background = "#00000000",

            # Margin
            margin = [9, 15, 0, 15],

            # Transparency
            opacity = 1,
        ),
    ),

    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        top = bar.Bar(
            # Source in widgets.py
            widgets_tmp,

            # Bar Size
            20,

            # Background Color
            background = "#00000000",

            # Margin
            margin = [9, 15, 0, 15],

            # Transparency
            opacity = 1,
        ),
    ),
]
