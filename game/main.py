import getpass

from game.world import World

worlds = [World(f"/home/{getpass.getuser()}/.the_storm/world1.json"), World(f"/home/{getpass.getuser()}/.the_storm/world2.json"), World(f"/home/{getpass.getuser()}/.the_storm/world3.json")]


def game_main(world: int):
    worlds[world].open()
