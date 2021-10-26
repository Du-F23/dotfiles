# --==[ Colorschemes ]==--

import json
from .settings import theme_path

# Theme settings
file = open(theme_path, 'r')
content = file.read()
theme = json.loads(content)
file.close()

hex = {
    # Layouts
    'normal': theme['normal'],
    'border': theme['border'],

    # Workspaces
    'active': theme['active'],
    'inactive': theme['inactive'],
    'focus': theme['focus'],

    # Bar
    'center': theme['center'],
    'base1': theme['base1'],
    'base2': theme['base2'],
    'base3': theme['base3'],
    'base4': theme['base4'],
    'base5': theme['base5'],

    # Text & Icons
    'text': theme['text'],
    'color1': theme['color1'],
    'color2': theme['color2'],
    'color3': theme['color3'],
    'color4': theme['color4'],
}
