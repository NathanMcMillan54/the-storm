#!/bin/bash

mkdir ~/.the_storm/
python3 tools/generate_world.py && mv world.json ~/.the_storm/world1.json
python3 tools/generate_world.py && mv world.json ~/.the_storm/world2.json
python3 tools/generate_world.py && mv world.json ~/.the_storm/world3.json

exit 0
mv The_Storm.desktop ~/Desktop/
sudo mv The_Storm.linux.x86_64 /bin/
