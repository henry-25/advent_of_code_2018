import pprint

class goblin:

    kind = 'goblin'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack_power = 3
        self.hit_points = 200

    def __repr__(self):
        # return 'Goblin (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Goblin'

    def __str__(self):
        # return 'Goblin (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Goblin'
    
    def move(self, direction):
        if(direction == 'north'):
            self.y += 1
        elif(direction == 'south'):
            self.y -= 1
        elif(direction == 'west'):
            self.x -= 1
        elif(direction == 'east'):
            self.x += 1
        else:
            print('Invalid direction', direction)
    
    def identify_target(self, current_grid):
        closest_target = 999
        for line in current_grid:
            for i in line:
                # print((x, y), i.kind)
                if i.kind == 'elf':
                    find_distance(self, i, current_grid)

class elf:

    kind = 'elf'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack_power = 3
        self.hit_points = 200

    def __repr__(self):
        # return 'Elf (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Elf'

    def __str__(self):
        # return 'Elf (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Elf'

    def move(self, direction):
        if(direction == 'north'):
            self.y += 1
        elif(direction == 'south'):
            self.y -= 1
        elif(direction == 'west'):
            self.x -= 1
        elif(direction == 'east'):
            self.x += 1
        else:
            print('Invalid direction', direction)

class wall:

    kind = 'wall'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # return 'Wall (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Wall'

    def __str__(self):
        # return 'Wall (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Wall'

class open_space:

    kind = 'open_space'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # return 'Open space (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Open'

    def __str__(self):
        # return 'Open space (' + str(self.x) + ', ' + str(self.y) + ')'
        return 'Open'

def file_len(fname):
    line_len = 0
    with open(fname) as f: 
        for i, l in enumerate(f):
            line_len = len(l)
            pass
    return i + 1, line_len + 1

def find_distance(unit_source, unit_target, current_grid):
    print(unit_source, (unit_source.x, unit_source.y), unit_target, (unit_target.x, unit_target.y))

def main():
    
    f_len, l_len = file_len('input_example.txt')

    grid_representation = [['.' for i in range(l_len - 1)] for j in range(f_len)]

    with open('input_example.txt') as f:
        for y, line in enumerate(f):
            for x, i in enumerate(line):
                try:
                    if i == '#':
                        grid_representation[y][x] = wall(x, y)
                    elif i == '.':
                        grid_representation[y][x] = open_space(x, y)
                    elif i == 'G':
                        grid_representation[y][x] = goblin(x, y)
                    elif i == 'E':
                        grid_representation[y][x] = elf(x, y)
                except: 
                    pass

    for i in grid_representation:
        for j in i:
            try:
                if j.kind == 'goblin' or j.kind == 'elf':
                    j.identify_target(grid_representation)
            except:
                pass

    # pprint.pprint(grid_representation)

if __name__ == "__main__":
    main()