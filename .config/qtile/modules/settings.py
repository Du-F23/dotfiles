# --==[ Settings ]==--

from os import path

# General
mod = 'mod4'
terminal = 'st'
browser = 'firefox'
file_manager = 'thunar'
font = 'SauceCodePro Nerd Font Medium'
wallpaper = '~/wallpapers/wp1.png'

# Weather
location = {'Mexico': 'Mexico'}
city = 'Mexico City, MX'

# Hardware [/sys/class]
net = 'wlp2s0'
backlight = 'radeon_bl0'

# Color Scheme
colorscheme = 'material_ocean'
directory = path.join(path.expanduser('~'), '.config/qtile/schemes/')
scheme_path = directory + colorscheme + '.json'
