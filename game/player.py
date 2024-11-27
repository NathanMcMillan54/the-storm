import random
import pygame

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Player:
    def __init__(self, color):
        self.health = 100.0
        self.alive = True
        self.mx = 0
        self.my = 0
        self.x = 8
        self.y = random.randint(28, 32)
        self.right = True
        self.use_item = False
        self.inventory = []
        self.inventory_item_selected = 0
        self.inventory_open = False
        self.ci = [0] * 10
        self.selected_item = 0
        self.color = color
