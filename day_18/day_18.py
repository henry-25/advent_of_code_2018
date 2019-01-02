import pprint

def part_one():
    width, height = 50, 50
    open_space = [['.' for x in range(width)] for y in range(height)]
    minutes_passed = 1
    
    with open('input.txt') as input_file:
        for line_count, line in enumerate(input_file):
            for char_count, char in enumerate(line):
                if line_count < 50 and char_count < 50:
                    open_space[line_count][char_count] = char

    while minutes_passed < 1000000001:
        print('Minute', minutes_passed)
        mid_change = [['.' for x in range(width)] for y in range(height)]
        for line_num, line in enumerate(open_space):
            for spot_num, spot in enumerate(line):
                num_adjacent_trees, num_adjacent_lumberyards = 0, 0
                if line_num > 0:
                    # Top left diagonal
                    if spot_num > 0:
                        if open_space[line_num - 1][spot_num - 1] == '|':
                            num_adjacent_trees += 1
                        if open_space[line_num - 1][spot_num - 1] == '#':
                            num_adjacent_lumberyards += 1
                    # Top right diagonal
                    if spot_num < 49:
                        if open_space[line_num - 1][spot_num + 1] == '|':
                            num_adjacent_trees += 1
                        if open_space[line_num - 1][spot_num + 1] == '#':
                            num_adjacent_lumberyards += 1
                    # Space above
                    if open_space[line_num - 1][spot_num] == '|':
                        num_adjacent_trees += 1
                    if open_space[line_num - 1][spot_num] == '#':
                        num_adjacent_lumberyards += 1
                if line_num < 49:
                    # Bottom left diagonal
                    if spot_num > 0:
                        if open_space[line_num + 1][spot_num - 1] == '|':
                            num_adjacent_trees += 1
                        if open_space[line_num + 1][spot_num - 1] == '#':
                            num_adjacent_lumberyards += 1
                    # Bottom right
                    if spot_num < 49:
                        if open_space[line_num + 1][spot_num + 1] == '|':
                            num_adjacent_trees += 1
                        if open_space[line_num + 1][spot_num + 1] == '#':
                            num_adjacent_lumberyards += 1
                    # Space below
                    if open_space[line_num + 1][spot_num] == '|':
                        num_adjacent_trees += 1
                    if open_space[line_num + 1][spot_num] == '#':
                        num_adjacent_lumberyards += 1
                if spot_num > 0:
                    # Space left
                    if open_space[line_num][spot_num - 1] == '|':
                        num_adjacent_trees += 1
                    if open_space[line_num][spot_num - 1] == '#':
                        num_adjacent_lumberyards += 1
                if spot_num < 49:
                    # Space right
                    if open_space[line_num][spot_num + 1] == '|':
                        num_adjacent_trees += 1
                    if open_space[line_num][spot_num + 1] == '#':
                        num_adjacent_lumberyards += 1
                # Convert open space to tree space
                if spot == '.' and num_adjacent_trees > 2:
                    mid_change[line_num][spot_num] = '|'
                # Convert tree space to lumberyard space
                elif spot == '|' and num_adjacent_lumberyards > 2:
                    mid_change[line_num][spot_num] = '#'
                # Convert lumber yard to open
                elif spot == '#' and (num_adjacent_lumberyards < 1 or num_adjacent_trees < 1):
                    mid_change[line_num][spot_num] = '.'
                else:
                    mid_change[line_num][spot_num] = spot
                # print(line_num, spot_num, spot, 'Adjacent trees:', num_adjacent_trees, 'Adjacent lumberyards:', num_adjacent_lumberyards)
        open_space = mid_change
        # pprint.pprint(open_space)
        minutes_passed += 1

    num_resource_trees = 0
    num_resource_lumberyards = 0
    for line in open_space:
        for spot in line:
            if spot == '|':
                num_resource_trees += 1
            if spot == '#':
                num_resource_lumberyards += 1
                
    print(num_resource_trees)
    print(num_resource_lumberyards)
    print(num_resource_trees * num_resource_lumberyards)

if __name__ == "__main__":
    part_one()