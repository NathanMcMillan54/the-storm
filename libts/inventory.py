from libts.block import NULL_BLOCK
from libts.item import Item, ITEMS

class InventoryData:
    def __init__(self):
        empty_item = InventoryItem()
        self.current_inventory = [empty_item.__dict__ for _item in range(10)] # Block ids
        self.stored_inventory = [empty_item.__dict__ for _item in range(20)] # Block ids
        
    def from_dict(self, inventory_dict):
        self.current_inventory = inventory_dict['current_inventory']
        self.stored_inventory = inventory_dict['stored_inventory']

class InventoryItem:
    def __init__(self):
        self.item_id = 0
        self.item_count = 0

    def from_dict(self, item_dict):
        self.item_id = item_dict['item_id']
        self.item_count = item_dict['item_count']
