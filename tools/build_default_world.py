def main():
    world_file = open("default_world.json", "w+")

    world_file.writelines("{\n")

    for y in range(61):
        value = 0
        world_file.writelines(f"\t\"y{y}\": {{\n")

        if y < 30:
            value = 0
        elif y == 31 or y == 32:
            value = 1
        elif y > 32:
            value = 2

        for x in range(111):
            if x == 110:
                world_file.writelines(f"\t\t\"x{x}\": {value}\n")
            else:
                world_file.writelines(f"\t\t\"x{x}\": {value},\n")

        if y == 60:
            world_file.writelines("\t}\n")
        else:
            world_file.writelines("\t},\n")

    world_file.writelines("}\n")


if __name__ == '__main__':
    main()
