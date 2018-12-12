def main():
    grid_serial_number = 2568
    max_power_level = 0
    max_power_corner = (0, 0)

    for x in range(1, 299):
        for y in range(1, 299):
            curr_corner_power = find3by3PowerLevel(x, y, grid_serial_number)
            if curr_corner_power > max_power_level:
                max_power_level = curr_corner_power
                max_power_corner = (x, y)
                print(max_power_level)
                print(max_power_corner)


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

def find3by3PowerLevel(x, y, grid_serial_number):
    total_power_level = 0
    for add_x in range(3):
        for add_y in range(3):
            total_power_level += findPowerLevel(x + add_x, y + add_y, grid_serial_number)
    return total_power_level


if __name__ == "__main__":
    main()