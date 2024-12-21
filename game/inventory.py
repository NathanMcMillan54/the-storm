from libts.item import ITEMS, NULL_BLOCK

class Inventory:
    def __init__(self):
        self.current_items = [ITEMS[NULL_BLOCK] for _item in range(10)]
        self.stored_items = [ITEMS[NULL_BLOCK] for _item in range(20)]

    def from_inventory_data(self, inventory_data):
        for ci in range(len(inventory_data.current_inventory)):
            item = ITEMS[inventory_data.current_inventory[ci]['item_id']]
            item.count = inventory_data.current_inventory[ci]['item_count']
            self.current_items[ci] = item
        
        for si in range(len(inventory_data.stored_inventory)):
            item = ITEMS[inventory_data.stored_inventory[si]['item_id']]
            item.count = inventory_data.stored_inventory[si]['item_count']
            self.stored_items[si] = item
