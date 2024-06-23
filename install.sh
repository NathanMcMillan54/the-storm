#!/bin/bash

echo "Generating files..."
mkdir /home/$USER/.the_storm/
python3 tools/generate_world.py && mv world.json /home/$USER/.the_storm/world1.json
python3 tools/generate_world.py && mv world.json /home/$USER/.the_storm/world2.json
python3 tools/generate_world.py && mv world.json /home/$USER/.the_storm/world3.json
echo "Building The Storm"
pyinstaller main.spec

cp -r TheStorm.desktop /home/$USER/Desktop/
sudo mv dist/The_Storm /bin/The_Storm.bin
