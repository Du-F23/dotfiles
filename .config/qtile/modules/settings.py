# --==[ Settings ]==--

from os import path

# General
mod = 'mod4'
terminal = 'alacritty'
browser = 'firefox'
file_manager = 'thunar'
font = 'SauceCodePro Nerd Font Medium'

# Weather
location = {'Ecatzingo': 'Ecatzingo'}
city = 'Mexico City, MX'

# Hardware [/sys/class]
net = 'wlp2s0'
backlight = 'radeon_bl0'

# Color Scheme
file = 'material_ocean_dark.json'
directory = path.join(path.expanduser('~'), ".config/qtile/colorschemes/")
theme_path = directory + file

# Wallpaper
img = 'minimalist_wp1.jpg'
folder = '~/wallpapers/'
wallpaper = folder + img
