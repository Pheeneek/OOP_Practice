from py200_1_1 import Glass, GlassAddRemove


def main():
    # glass1 = Glass()
    # glass2 = Glass(500)
    # glass3 = Glass(500, 100)
    # print(glass1)
    # print(glass2)
    # print(glass3)
    #
    # list_glasses = [glass1, glass2, glass3]
    #
    # print(list_glasses)
    #
    # glass1.capacity_volume = 1000
    #
    # print(list_glasses)

    glass = GlassAddRemove(500, 0)
    print(glass.occupied_volume)
    print(f"over {glass.add_water(200)}")
    print(glass.occupied_volume)
    print("_________")
    print(glass.occupied_volume)
    print(f"over {glass.add_water(900)}")
    print(glass.occupied_volume)

    print("_________")
    print(glass.remove_water(600))
    print(glass.occupied_volume)

    print(dir(GlassAddRemove))


if __name__ == "__main__":
    main()

