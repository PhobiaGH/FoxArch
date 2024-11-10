#!/bin/bash

gksu cp /etc/foxarch/config/waybar/style_blacked.css ~/.config/waybar/style.css

killall waybar

if [[ $USER = "foxer" ]]
then
  waybar -c ~/.config/waybar/config & -s ~/.config/waybar/style.css
else
  waybar &
fi
