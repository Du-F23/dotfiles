#!/bin/sh

# Dual monitor
function monitors() {
  local monitor='HDMI-0 connected'
  local output=$(xrandr | grep -o "${monitor}")

  if [[ $output == $monitor ]]; then
    xrandr --output eDP --primary --auto --output HDMI-0 --auto --left-of eDP
  else
    xrandr --output eDP --primary --auto --output HDMI-0 --off
  fi
}; monitors

# Keyboard layout
setxkbmap us -variant altgr-intl

# Screensaver
xset -dpms s off

# Compositor
picom &

# Start WM
exec qtile start
