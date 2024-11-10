#bin/sh

if [ -f "/usr/bin/swayidle" ]; then
	echo "swayidle is installed."
	swayidle -w timeout 500 'swaylock -f' #timeout 150 'hyprctl dispatch dpms off' resume 'hyprctl dispatch dpms on' # Uncomment "timeout 550" if on bare bones
else
	echo "swayidle is not installed."
fi;
