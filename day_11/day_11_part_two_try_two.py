def main():
    grid_serial_number = 2568
    max_power_level = -999
    max_power_corner = (0,0)
    max_power_size = -999
    grid_power_level = dict()

    # for x in range(1, 300):
    #     for y in range(1, 300):
    #         grid_power_level[(x, y)] = findPowerLevel(x, y, grid_serial_number)

    for x in range(1, 301):
        for y in range(1, 301):
            max_size = 0
            if x < y:
                max_size = 301 - y
            else:
                max_size = 301 - x
            curr_power = 0
            for i in range(1, max_size):     
                print((x, y), i, (x + i, y + i))
            # for size in range(3, 300):
                # print(x,y,size)
                # if x + size > 300 or y + size > 300:
                #     pass
                # else:
            # max_size = min(300 - x, 300 - y)
            # print(x, y, max_size)
            # curr_corner_power, ms = findSquarePowerLevel(x, y, max_size, grid_power_level)
            # if (curr_corner_power > max_power_level):
            #     max_power_level = curr_corner_power
            #     max_power_corner = (x, y)
            #     max_power_size = ms
    
    print(max_power_corner)
    print(max_power_size)


def findPowerLevel(x, y, grid_serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = (power_level % 1000)
    if power_level < 100:
        power_level = 0
    else:
        power_level = int(str(power_level)[0])
    power_level -= 5
    return power_level

def findSquarePowerLevel(x, y, max_size, grid_power_level):
    max_power_level = 0
    max_power_size = 0
    curr_size_power = 0
    for i in range(max_size):
        curr_size_power += findOuterRingPowerLevel(x, y, i, grid_power_level)
        if curr_size_power > max_power_level:
            max_power_size = i
            max_power_level = curr_size_power
    return max_power_size, max_power_level

def findOuterRingPowerLevel(x, y, size, grid_power_level):
    power_level = 0
    for x in range(3, size - 3):
        power_level += grid_power_level[(x, y + size - 3)]
    for y in range(3, size - 4):
        power_level += grid_power_level[(x + size - 3, y)]
    return power_level
    


if __name__ == "__main__":
    main()