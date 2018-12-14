import pprint

def main():
    cart_grid = [['' for x in range(160)] for y in range(160)]
    carts_active = {}
    num_carts = 0
    collision_occurred = False

    with open('input.txt') as input_file:
        for y, line in enumerate(input_file):
            for x, char in enumerate(line):
                if char:
                    if char == '>':
                        num_carts += 1
                        carts_active[num_carts] = {'current_location': (y, x), 'current_direction': 'right', 'next_turn': 'left'}
                        char = '-'
                    if char == '<':
                        num_carts += 1
                        carts_active[num_carts] = {'current_location': (y, x), 'current_direction': 'left', 'next_turn': 'left'}
                        char = '-'
                    if char == 'v':
                        num_carts += 1
                        carts_active[num_carts] = {'current_location': (y, x), 'current_direction': 'down', 'next_turn': 'left'}
                        char = '|'
                    if char == '^':
                        num_carts += 1
                        carts_active[num_carts] = {'current_location': (y, x), 'current_direction': 'up', 'next_turn': 'left'}
                        char = '|'
                    cart_grid[y][x] = char
    num_ticks = 0

    while not collision_occurred and num_ticks < 112:
        sorted(carts_active, key=lambda k: (carts_active[k]['current_location'][0], carts_active[k]['current_location'][1]))
        for cart in carts_active:
            # print(num_ticks, carts_active[cart])
            make_move(cart, carts_active, cart_grid)
            collision_occurred = check_collision(carts_active, num_ticks)
        num_ticks += 1

    pprint.pprint(carts_active)

    with open('grid.txt', 'a') as f:
        print(cart_grid, file=f)
    # pprint.pprint(cart_grid)

def make_move(cart, carts_active, cart_grid):
    (y, x) = carts_active[cart]['current_location']
    current_direction = carts_active[cart]['current_direction']
    next_turn = carts_active[cart]['next_turn']
    direction = cart_grid[y][x]
    if direction == '-':
        if current_direction == 'right':
            x = x + 1
        elif current_direction == 'left':
            x = x - 1
        else:
            print('Invalid directions')
    if direction == '|':
        if current_direction == 'up':
            y = y - 1
        elif current_direction == 'down':
            y = y + 1
        else:
            print('Invalid directions')
    if direction == '\\':
        if current_direction == 'up':
            carts_active[cart]['current_direction'] = 'left'
            x = x - 1
        elif current_direction == 'down':
            carts_active[cart]['current_direction'] = 'right'
            x = x + 1
        elif current_direction == 'right':
            carts_active[cart]['current_direction'] = 'down'
            y = y + 1
        elif current_direction == 'left':
            carts_active[cart]['current_direction'] = 'up'
            y = y - 1
        else:
            print('Invalid directions')
    if direction == '/':
        if current_direction == 'up':
            carts_active[cart]['current_direction'] = 'right'
            x = x + 1
        elif current_direction == 'down':
            carts_active[cart]['current_direction'] = 'left'
            x = x - 1
        elif current_direction == 'right':
            carts_active[cart]['current_direction'] = 'up'
            y = y - 1
        elif current_direction == 'left':
            carts_active[cart]['current_direction'] = 'down'
            y = y + 1
        else:
            print('Invalid directions')
    if direction == '+':
        if current_direction == 'up':
            if next_turn == 'left':
                x = x - 1
                carts_active[cart]['current_direction'] = 'left'
                next_turn = 'straight'
            elif next_turn == 'straight':
                y = y - 1
                next_turn = 'right'
            elif next_turn == 'right':
                x = x + 1
                carts_active[cart]['current_direction'] = 'right'
                next_turn = 'left'
            else:
                print('Uncaught direction error')
        if current_direction == 'down':
            if next_turn == 'left':
                x = x + 1
                carts_active[cart]['current_direction'] = 'right'
                next_turn = 'straight'
            elif next_turn == 'straight':
                y = y + 1
                next_turn == 'right'
            elif next_turn == 'right':
                x = x - 1
                carts_active[cart]['current_direction'] = 'left'
                next_turn == 'left'
            else:
                print('Invalid directions')
        if current_direction == 'right':
            if next_turn == 'left':
                y = y - 1
                carts_active[cart]['current_direction'] = 'up'
                next_turn = 'straight'
            elif next_turn == 'straight':
                x = x + 1
                next_turn = 'right'
            elif next_turn == 'right':
                y = y + 1
                carts_active[cart]['current_direction'] = 'down'
                next_turn = 'left'
            else:
                print('Uncaught direction error')
        if current_direction == 'left':
            if next_turn == 'left':
                y = y + 1
                carts_active[cart]['current_direction'] = 'down'
                next_turn = 'straight'
            elif next_turn == 'straight':
                x = x - 1
                next_turn = 'right'
            elif next_turn == 'right':
                y = y - 1
                carts_active[cart]['current_direction'] = 'up'
                next_turn = 'left'
            else:
                print('Uncaught direction error')
    carts_active[cart]['next_turn'] = next_turn
    carts_active[cart]['current_location'] = (y, x)
    
def check_collision(carts_active, num_ticks):
    for key_a in carts_active:
        for key_b in carts_active:
            if key_a == key_b:
                break
            if carts_active[key_a]['current_location'] == carts_active[key_b]['current_location']:
                print(carts_active[key_a]['current_location'], num_ticks)
                return True
    return False


if __name__ == "__main__":
    main()