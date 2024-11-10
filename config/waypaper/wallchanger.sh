#!/bin/bash

if [ -f "/usr/bin/waypaper" ]; then
	echo "waypaper is installed."
	waypaper --random
else
	echo "waypaper is not installed."
fi;
