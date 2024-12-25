import random

RIGHT = 0
LEFT = 1
UP = 2
ATTACK = 3
NOTHING = 4

class Npc:
    def __init__(self, hostile, color, health, damage):
        self.hostile = hostile
        self.color = color
        self.health = health
        self.damage = damage
        self.moving_right = False
        self.standing_still = True
        self.x = random.randint(40, 100)
        self.y = random.randint(15, 25)
        self.action = NOTHING
    
    def update(self, player):
        if self.x == 0:
            self.action == RIGHT
            self.x += 1
            return
        elif self.x >= 90:
            self.action == LEFT
            self.x -= 1
            return

        actions = []
        if self.hostile:
            x_diff = player.x - self.x
            if abs(x_diff) > 10:
                for _i in range(4):
                    actions.append(NOTHING)
                actions.append(LEFT)
                actions.append(RIGHT)
                actions.append(UP)
            elif x_diff > 0:
                for _i in range(4):
                    actions.append(RIGHT)
            elif x_diff < 0:
                for _i in range(4):
                    actions.append(LEFT)
            else:
                actions.append(ATTACK)
        else:
            for _i in range(4):
                actions.append(NOTHING)
            for _i in range(2):
                actions.append(LEFT)
                actions.append(RIGHT)
            actions.append(UP)
        
        self.action = random.choice(actions)

        if self.action == LEFT:
            self.x -= 1
        elif self.action == RIGHT:
            self.x += 1
        elif self.action == UP:
            self.y += 1
        elif self.action == NOTHING:
            self.x = self.x
        elif self.action == ATTACK:
            if self.x == player.x:
                player.health -= self.damage
