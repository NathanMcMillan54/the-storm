import os

from setup.errors import errors, error_message


def check_files():
    global errors
    global error_message

    if os.path.exists("~/.the_storm/world1.json"):
        errors = True
        error_message = "Error: world1 file not found"
    elif os.path.exists("~/.the_storm/world2.json"):
        errors = True
        error_message = "Error: world2 file not found"
    elif os.path.exists("~/.the_storm/world3.json"):
        errors = True
        error_message = "Error: world3 file not found"
