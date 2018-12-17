import pprint

def main(): 
    clay_spots = []
    water_source = (500, 0)
    min_x = water_source[0]
    min_y = water_source[1]
    max_x = water_source[0]
    max_y = water_source[1]

    with open('input_example.txt') as f:
        for line in f:
            coords = line.split(',')
            const = coords[0].strip().split('=')
            ran = coords[1].strip().split('=')
            if ran[0] == 'y':
                extremes = ran[1].split('..')
                for i in range(int(extremes[0]), int(extremes[1]) + 1):
                    tuple_append = (int(const[1]), i)
                    clay_spots.append(tuple_append)
                    min_x = int(const[1]) if int(const[1]) < min_x else min_x
                    min_y = i if i < min_y else min_y
                    max_x = int(const[1]) if int(const[1]) > max_x else max_x
                    max_y = i if i > max_y else max_y
            else:
                extremes = ran[1].split('..')
                for i in range(int(extremes[0]), int(extremes[1])):
                    tuple_append = (i, int(const[1]))
                    clay_spots.append(tuple_append)
                    min_x = i if i < min_x else min_x
                    min_y = int(const[1]) if int(const[1]) < min_y else min_y
                    max_x = i if i > max_x else max_x
                    max_y = int(const[1]) if int(const[1]) > max_y else max_y

    grid = [['.' for x in range(min_x - 2, max_x + 2)] for y in range(min_y - 2, max_y + 2)]
    grid[water_source[1] - min_y + 1][water_source[0] - min_x + 1] = '+'

    for entry in clay_spots:
        grid[entry[1] - min_y + 1][entry[0] - min_x + 1] = '#'

    curr_x, curr_y = water_source
    curr_x = curr_x - min_x + 1
    curr_y = curr_y - min_y + 2

    while True:
        if not grid[curr_y][curr_x] == '#':
            grid[curr_y][curr_x] = '|'
            curr_y += 1
        else:
            break

    pprint.pprint(grid)

    # print(water_source)
    # print(clay_spots)
    # print('Min X:', min_x)
    # print('Min Y:', min_y)
    # print('Max X:', max_x)
    # print('Max Y:', max_y)

if __name__ == "__main__":
    main()