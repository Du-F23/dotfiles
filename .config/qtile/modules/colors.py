# --==[ Colors ]==--

import json
from .settings import scheme_path

# Scheme settings
file = open(scheme_path, 'r')
content = file.read()
color = json.loads(content)
file.close()

hex = {
    # Layouts
    'normal': color['normal'],
    'border': color['border'],

    # Workspaces
    'active': color['active'],
    'inactive': color['inactive'],
    'focus': color['focus'],

    # Bar
    'center': color['center'],
    'base1': color['base1'],
    'base2': color['base2'],
    'base3': color['base3'],
    'base4': color['base4'],
    'base5': color['base5'],

    # Text & Icons
    'text': color['text'],
    'color1': color['color1'],
    'color2': color['color2'],
    'color3': color['color3'],
    'color4': color['color4'],
}
