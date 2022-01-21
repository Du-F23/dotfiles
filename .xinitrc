#!/bin/sh

xrandr --output HDMI-0 --auto --left-of eDP --output eDP --primary --auto

exec qtile start
