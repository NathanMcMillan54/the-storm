#!/bin/bash

echo "Generating files..."
mkdir /home/$USER/.the_storm/
python3 tools/generate_world.py && mv world.json /home/$USER/.the_storm/world1.json
python3 tools/generate_world.py && mv world.json /home/$USER/.the_storm/world2.json
python3 tools/generate_world.py && mv world.json /home/$USER/.the_storm/world3.json
