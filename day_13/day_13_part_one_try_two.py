import pprint

class Cart:
    def __init__(self, curr_position, curr_direction):
        self.position = curr_position
        self.direction = curr_direction
        self.next_turn = 'left'
    def __repr__(self):
        return str(self.position)


def createGridGetCarts(input_file):
    tracks = dict()
    carts = []
    with open(input_file) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == '\n':
                    continue
                if char in '<v>^':
                    direction = {
                        '<': 'left',
                        'v': 'down',
                        '>': 'right',
                        '^': 'up',
                    }[char]
                    carts.append(Cart((x,y), direction))
                    part = {
                        '<': '-',
                        'v': '|',
                        '>': '-',
                        '^': '|',
                    }[char]
                else:
                    part = char
                if part in '\\/+':
                    tracks[(x,y)] = part
    return tracks, carts
                        
def turnCart(cart, part):
    if not part:
        return
    if part == '\\':
        if cart.direction == 'up':
            cart.direction = 'left'
        elif cart.direction == 'down':
            cart.direction = 'right'
        elif cart.direction == 'left':
            cart.direction = 'up'
        else:
            cart.direction = 'down'
    if part == '/':
        if cart.direction == 'up':
            cart.direction = 'right'
        elif cart.direction == 'down':
            cart.direction = 'left'
        elif cart.direction == 'left':
            cart.direction = 'down'
        else:
            cart.direction = 'up'
    if part == '+':
        if cart.direction == 'up':
            if cart.next_turn == 'left':
                cart.direction = 'left'
                cart.next_turn = 'straight'
            elif cart.next_turn == 'straight':
                cart.next_turn = 'right'
            else:
                cart.direction = 'right'
                cart.next_turn = 'left'
        elif cart.direction == 'down':
            if cart.next_turn == 'left':
                cart.direction = 'right'
                cart.next_turn = 'straight'
            elif cart.next_turn == 'straight':
                cart.next_turn = 'right'
            else:
                cart.direction = 'left'
                cart.next_turn = 'left'
        elif cart.direction == 'left':
            if cart.next_turn == 'left':
                cart.direction = 'down'
                cart.next_turn = 'straight'
            elif cart.next_turn == 'straight':
                cart.next_turn = 'right'
            else:
                cart.direction = 'up'
                cart.next_turn = 'left'
        else:
            if cart.next_turn == 'left':
                cart.direction = 'up'
                cart.next_turn = 'straight'
            elif cart.next_turn == 'straight':
                cart.next_turn = 'right'
            else:
                cart.direction = 'down'
                cart.next_turn = 'left'

def moveCart(cart):
    if cart.direction == 'up':
        cart.position = (cart.position[0] - 1, cart.position[1])
    elif cart.direction == 'down':
        cart.position = (cart.position[0] + 1, cart.position[1])
    elif cart.direction == 'right':
        cart.position = (cart.position[0], cart.position[1] + 1)
    else:
        cart.position = (cart.position[0], cart.position[1] - 1)


def main():
    cart_grid, carts_active = createGridGetCarts('input.txt')
    num_ticks = 0
    while True:
        carts_active.sort(key=lambda k: (k.position[0], k.position[1]))
        for ci, cart in enumerate(carts_active):
            moveCart(cart)
            if any(c2.position == cart.position for c2i, c2 in enumerate(carts_active) if c2i != ci):
                print(num_ticks)
                print(cart)
                return cart
            try:
                part = cart_grid[cart.position]
                turn_cart(cart, part)
            except:
                pass
        num_ticks += 1


if __name__ == "__main__":
    main()
    