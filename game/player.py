import random
import pygame

from libts.inventory import InventoryData
from game.inventory import Inventory

PLAYER_SIZE = (10, 20)

class Player:
    def __init__(self, color):
        self.health = 100.0
        self.alive = True
        self.mx = 0
        self.my = 0
        self.x = 8
        self.y = 10
        self.right = True
        self.use_item = False
        self.inventory = Inventory()
        self.inventory_item_selected = 0
        self.inventory_open = False
        self.ci = [0] * 10
        self.selected_item = 0
        self.color = color
