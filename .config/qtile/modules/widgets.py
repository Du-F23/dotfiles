# --==[ Widgets ]==--

from libqtile import widget

from .colorscheme import hex
from .settings import font, interface, backlight

icon_font = 'SauceCodePro Nerd Font'

# General bar settings
widget_defaults = dict(
    font = font,
    fontsize = 10,
    padding = 4,
)
extension_defaults = widget_defaults.copy()

# Functions
def base(bg, fg):
    return {
        'background': bg,
        'foreground': fg,
    }

def font_config(fontsize):
    return {
        'font': icon_font,
        'fontsize': fontsize,
    }

def sep(fg):
    if fg != '':
        return widget.TextBox(
            **base(None, fg),
            **font_config(15),
            padding = 12,
            text = '')
    else:
        fg = '#000000'
        return widget.TextBox(
            **base(None, fg),
            **font_config(5),
            padding = 1,
            text = ' ')

def spacer(bg):
    return widget.Spacer(
        background = bg
    )

def side(fg, side):
    if side == 'right': icon = ''
    elif side == 'left': icon = ''
    else: icon = ''
    return widget.TextBox(
        **base(None, fg),
        **font_config(15),
        padding = 0,
        text = icon)

def fix_padding(bg):
    return widget.TextBox(
        **font_config(11),
        background = bg,
        padding = -1,
        text = ' ')

def icon(bg, fg, icon):
    return widget.TextBox(
        **base(bg, fg),
        **font_config(13),
        padding = 3,
        text = icon)

def alt_fg(fg, icon_fg):
    if icon_fg == '':
        return fg
    else:
        return icon_fg

# Modules
def battery(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        widget.Battery(
            **base(bg, icon_fg),
            **font_config(13),
            format = '{char}',
            charge_char = 'ﮣ',
            discharge_char = ' ',
            full_char = '',
            low_percentage = 0.3,
            low_foreground = '#FF0000',
            padding = None,
            update_interval = 60),
        widget.Battery(
            **base(bg, fg),
            format = '{percent:2.0%}',
            low_foreground = fg,
            padding = None,
            update_interval = 60),
        side(bg, 'right'),
    ]

def brightness(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ' '),
        widget.Backlight(
            **base(bg, fg),
            backlight_name = backlight,
            format = '{percent:2.0%}',
            padding = 0,
            update_interval = 0.2),
        fix_padding(bg),
        side(bg, 'right'),
    ]

def clock(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ' '),
        widget.Clock(
            **base(bg, fg),
            format = '%A, %b %-d, %I:%M %p',
            padding = 0,
            update_interval = 1.0),
        fix_padding(bg),
        side(bg, 'right'),
    ]

def cpu(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ''),
        widget.CPU(
            **base(bg, fg),
            format = '{load_percent:.0f}%',
            padding = None,
            update_interval = 1.0),
        side(bg, 'right'),
    ]

def disk(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ''),
        widget.DF(
            **base(bg, fg),
            format = '{uf}{m}',
            measure = 'G',
            padding = None,
            partition = '/',
            update_interval = 60,
            visible_on_warn = False,
            warn_color = '#ff0000'),
        side(bg, 'right'),
    ]

def groups(bg):
    return [
        widget.GroupBox(
            **font_config(10),
            background = bg,
            blockwidth = 2,
            margin_y = 3,
            rounded = True,
            hide_unused = False,
            disable_drag = True,
            use_mouse_wheel = False,
            active = hex['active'],
            inactive = hex['inactive'],
            highlight_method = 'text',
            this_current_screen_border = hex['focus']),
    ]

def group_number(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, '缾'),
        widget.AGroupBox(
            **base(bg, fg),
            borderwidth = 0,
            margin_y = 4,
            padding = 0),
        side(bg, 'right'),
    ]

def layout_icon():
    return widget.CurrentLayoutIcon(
        background = None,
        padding = 5,
        scale = 0.75)

def layout(bg, fg):
    return [
        side(bg, 'left'),
        widget.CurrentLayout(
            **base(bg, fg),
            padding = None),
        side(bg, 'right'),
    ]

def logo(bg, fg):
    return [
        side(bg, 'left'),
        widget.TextBox(
            **base(bg, fg),
            **font_config(13),
            padding = 10,
            text = ''),
        fix_padding(bg),
        side(bg, 'right'),
    ]

def quick_exit(bg, fg):
    return [
        side(bg, 'left'),
        widget.QuickExit(
            **base(bg, fg),
            **font_config(13),
            countdown_format='{}',
            countdown_start = 5,
            default_text = '襤',
            padding = 10,
            timer_interval = 1),
        side(bg, 'right'),
    ]

def ram(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, '﬙'),
        widget.Memory(
            **base(bg, fg),
            format = '{MemUsed: .0f}{mm}',
            measure_mem = 'M',
            padding = 0,
            update_interval = 1.0),
        fix_padding(bg),
        side(bg, 'right'),
    ]

def volume(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ''),
        widget.PulseVolume(
            **base(bg, fg),
            get_volume_command = None,
            limit_max_volume = True,
            padding = None,
            update_interval = 0.2),
        side(bg, 'right'),
    ]

def updates(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ' '),
        widget.CheckUpdates(
            **base(bg, fg),
            colour_have_updates = fg,
            colour_no_updates = fg,
            display_format = '{updates}',
            distro = 'Arch_checkupdates',
            no_update_string = '0',
            padding = 0,
            update_interval = 3600),
        fix_padding(bg),
        side(bg, 'right'),
    ]

def spotify(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, '阮 '),
        widget.Mpris2(
            **base(bg, fg),
            name = 'spotify',
            objname="org.mpris.MediaPlayer2.spotify",
            display_metadata = ['xesam:title', 'xesam:artist'],
            max_chars = 41,
            padding = 0,
            scroll_chars = None,
            scroll_interval = 0.5,
            stop_pause_text = 'Paused'),
        fix_padding(bg),
        side(bg, 'right'),
    ]

def weather(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ''),
        widget.OpenWeather(
            **base(bg, fg),
            format = '{main_temp:.0f}°{units_temperature}',
            location = 'Mexico City, MX',
            metric = True,
            padding = None,
            update_interval = 600),
        side(bg, 'right'),
    ]

def wifi_speed(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ''),
        widget.Net(
            **base(bg, fg),
            format = '{down} {up}',
            interface = interface,
            padding = None,
            update_interval = 1,
            use_bits = True),
        side(bg, 'right'),
    ]

def wifi(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'left'),
        icon(bg, icon_fg, ' '),
        widget.Wlan(
            **base(bg, fg),
            disconnected_message = 'Disconnected',
            format = 'Connected',
            interface = interface,
            padding = 0,
            update_interval = 5),
        fix_padding(bg),
        side(bg, 'right'),
    ]

# Layouts
main = [
    *logo('#ffffff', '#000000'),

    sep('#ffffff'),

    *cpu('#ffffff', '#000000', ''),
    sep(''),
    *ram('#ffffff', '#000000', ''),
    sep('#ffffff'), 
    *quick_exit('#ffffff', '#000000'),

    spacer(None),
    *groups(None),
    spacer(None),

    *brightness('#ffffff', '#000000', ''),
    sep(''),
    *volume('#ffffff', '#000000', ''),
    sep('#ffffff'),
    *clock('#ffffff', '#000000', ''),
]

widgets = main
