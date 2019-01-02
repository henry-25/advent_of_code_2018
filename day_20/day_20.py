from collections import defaultdict

def main():
    print('Start')
    input_regex = ''
    with open('input.txt') as input_file:
        for line in input_file:
            input_regex = line
    

    vector_movement = {
        'N': -1j,
        'S': 1j,
        'E': 1,
        'W': -1
    }

    positions = []
    curr_pos = 0 + 0j
    distance_from_source = defaultdict(int)

    for char in input_regex:
        if char == '$' or char == '^':
            pass
        elif char == '(':
            positions.append(curr_pos)
        elif char == ')':
            curr_pos = positions.pop()
        elif char == '|':
            curr_pos = positions[-1]
        elif char in {'N', 'S', 'W', 'E'}:
            new_pos = curr_pos + vector_movement[char]
            distance_from_source[new_pos] = min(
                distance_from_source.get(new_pos, distance_from_source[curr_pos] + 1),
                distance_from_source[curr_pos] + 1
            )
            curr_pos = new_pos

    print('Part 1:' + str(max(distance_from_source.values())))
    print('Part 2:' + str(sum(map(lambda x: x >= 1000, distance_from_source.values()))))

if __name__ == "__main__":
    main()