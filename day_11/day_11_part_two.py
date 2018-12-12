def main():
    grid_serial_number = 18
    max_power_level = -999
    max_power_corner = (0, 0)
    max_power_size = -999

    # print(findSquarePowerLevel(1, 1, 5, grid_serial_number))

    for x in range(1, 30):
        for y in range(1, 30):
            largest_square = 31 - x if x > y else 31 - y
            if largest_square > 2:
                curr_corner_power, size = findSquarePowerLevel(x, y, largest_square, grid_serial_number)
                print('x:', x, 'y:', y, 'curr_corner_power:', curr_corner_power, 'size:', size)
                if curr_corner_power > max_power_level:
                    max_power_level = curr_corner_power
                    max_power_size = size
                    max_power_corner = (x, y)
    
    print('max power level:', max_power_level)
    print('size:', size)
    print('max power corner:', max_power_corner)


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

def findSquarePowerLevel(x, y, size, grid_serial_number):
    total_power_level = 0
    max_power_level_from_corner = -999
    for square_size in range(size + 1):
        for x in range(size + 1):
            # print('X, y, square size', (x, square_size, square_size))
            total_power_level += findPowerLevel(x, square_size, grid_serial_number)
        for y in range(size + 1):
            # print('X, y, square size', (square_size, y, square_size))
            total_power_level += findPowerLevel(square_size, y, grid_serial_number)
        if total_power_level > max_power_level_from_corner:
            max_power_level_from_corner = total_power_level
        # total_power_level += findPowerLevel(x + add_val, y + add_val, grid_serial_number)
    return total_power_level, size

# def findSquarePowerLevel(x, y, size, grid_serial_number):
#     total_power_level = 0
#     for add_x in range(size):
#         for add_y in range(size):
#             total_power_level += findPowerLevel(x + add_x, y + add_y, grid_serial_number)
#     return total_power_level


if __name__ == "__main__":
    main()