#!/bin/bash

sh gen_worlds.sh
echo "Building The Storm"
pyinstaller main.spec

cp -r TheStorm.desktop /home/$USER/Desktop/
sudo mv dist/The_Storm /bin/The_Storm.bin
