#!/bin/bash

echo "Installing The Storm for x86_64 Linux"
mkdir ~/.the_storm/
python3 tools/generate_world.py && mv world.json ~/.the_storm/world1.json
python3 tools/generate_world.py && mv world.json ~/.the_storm/world2.json
python3 tools/generate_world.py && mv world.json ~/.the_storm/world3.json

cp -r linux/The_Storm.desktop ~/Desktop/
echo "Password required"
sudo cp -r linux/TheStorm.linux.x86_64 /bin/
echo "Finished installing"
