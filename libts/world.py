from getpass import getuser
import json
from libts.block import *
from libts.inventory import InventoryData

WORLD_HEIGHT = 60
WORLD_WIDTH = 110

class WorldData:
    def __init__(self):
        self.day = 0
        self.time = 0.0
        self.blocks = [[NULL_BLOCK for _y in range(110)] for _x in range(60)] # Block ids
        self.inventory_data = InventoryData()

    def open(self, file_name: str):
        world_file = open(f"/home/{getuser()}/.the_storm/worlds/{file_name}").read()
        world_json = json.loads(world_file)

        self.day = world_json['day']
        self.time = world_json['time']
        self.blocks = world_json['blocks']
        inventory_data = InventoryData()
        self.inventory_data = inventory_data.from_dict(world_json['inventory_data'])

    def to_json_dict(self):
        return {
            'day': self.day,
            'time': self.time,
            'blocks': self.blocks,
            'inventory_data': self.inventory_data.__dict__
        }

    def write(self, file_name: str):
        world_json = json.dumps(self.to_json_dict())
        world_file = open(f"/home/{getuser()}/.the_storm/worlds/{file_name}", "w")
        world_file.write(world_json)
