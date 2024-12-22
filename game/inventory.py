from libts.item import ITEMS, NULL_BLOCK
import copy

class Inventory:
    def __init__(self):
        self.current_items = []
        self.stored_items = []

    def from_inventory_data(self, inventory_data):
        for ci in range(len(inventory_data.current_inventory)):
            item = ITEMS[inventory_data.current_inventory[ci]['item_id']]
            item.count = inventory_data.current_inventory[ci]['item_count']
            print(item.count)
            self.current_items.append(copy.copy(item))
        
        for si in range(len(inventory_data.stored_inventory)):
            item = ITEMS[inventory_data.stored_inventory[si]['item_id']]
            item.count = inventory_data.stored_inventory[si]['item_count']
            self.stored_items.append(copy.copy(item))
