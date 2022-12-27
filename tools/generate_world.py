import random

sections = [
    [0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 2, 2, 8, 2, 2, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 8, 2, 2, 2, 2, 2, 2, 16, 2, 2, 8, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 8, 2, 2, 2, 2, 2, 15, 2, 2, 15, 2, 2, 2, 2, 8],
]


def main():
    world_file = open("world.json", "w+")

    world_file.writelines("{\n")
    value = 0

    for y in range(61):
        world_file.writelines(f"\t\"y{y}\": {{\n")

        for x in range(111):
            if y < 30:
                value = sections[0][random.randint(0, len(sections[0]) - 1)]
            elif 34 > y > 32:
                value = sections[1][random.randint(0, len(sections[1]) - 1)]
            elif 36 > y > 34:
                value = sections[2][random.randint(0, len(sections[2]) - 1)]
            elif 42 > y > 36:
                value = sections[3][random.randint(0, len(sections[3]) - 1)]
            elif y > 42:
                value = sections[4][random.randint(0, len(sections[4]) - 1)]

            if x == 110:
                world_file.writelines(f"\t\t\"x{x}\": {value}\n")
            else:
                world_file.writelines(f"\t\t\"x{x}\": {value},\n")

        world_file.writelines("\t},\n")

    world_file.writelines("\t\"day\": 0,\n")
    world_file.writelines("\t\"inventory\": [\n")

    for i in range(0, 20):
        if i == 19:
            world_file.writelines("\t[0, 1]\n]")
            break
        elif i == 0:
            world_file.writelines("\t[7, 1],\n")
        elif i == 1:
            world_file.writelines("\t[5, 1],\n")
        else:
            world_file.writelines("\t[0, 1],\n")

    world_file.writelines("}\n")


if __name__ == '__main__':
	main()
