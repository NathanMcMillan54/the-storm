from libts.block import NULL_BLOCK
from libts.item import Item, ITEMS
from typing import Optional

class InventoryData:
    def __init__(self):
        self.current_inventory = [NULL_BLOCK] * 10
        self.stored_inventory = [NULL_BLOCK] * 20
        
    def from_dict(self, inventory_dict):
        self.current_inventory = inventory_dict['current_inventory']
        self.stored_inventory = inventory_dict['stored_inventory']
