# Assembling items
from game.items import items


def assemble(citems):
    item_ids = []

    for item in citems:
        item_ids.append(item.id)

    if item_ids == asm_items[1]:
        return items[1]
    elif item_ids == asm_items[9]:
        return items[9]
    elif item_ids == asm_items[10]:
        return items[10]
    elif item_ids == asm_items[11]:
        return items[11]
    elif item_ids == asm_items[12]:
        return items[12]
    elif item_ids == asm_items[17]:
        return items[17]
    elif item_ids == asm_items[18]:
        return items[18]
    elif item_ids == asm_items[19]:
        return items[19]
    elif item_ids == asm_items[20]:
        return items[20]
    else:
        return items[0]


asm_items = {
    # Grass
    1: [0,
        0, 0, 0,
        0, 2, 2,
        0, 0, 0,
    ],
    # Cut up Ground Wood
    9: [0,
        0, 0, 0,
        0, 8, 0,
        0, 0, 0,
    ],
    # Sticks
    10: [
        0,
        0, 0, 0,
        0, 9, 0,
        0, 9, 0,
    ],
    # Door
    11: [0,
        0, 9, 9,
        0, 9, 9,
        0, 9, 9,
    ],
    # Ground Wood Wall
    12: [0,
        0, 0, 0,
        0, 9, 0,
        0, 0, 0,
    ],
    # Sword
    17: [0,
        0, 9, 0,
        0, 9, 0,
        0, 10, 0,
    ],
    # Sword
    18: [0,
        0, 15, 0,
        0, 15, 0,
        0, 10, 0,
    ],
    # Bow
    19: [0,
        16, 10, 0,
        16, 0, 10,
        16, 10, 0,
    ],
    # Arrow
    20: [0,
        0, 0, 0,
        0, 10, 15,
        0, 0, 0,
    ],
}
