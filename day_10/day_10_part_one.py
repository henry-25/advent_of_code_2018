import pprint

def main():
    points_tracker = dict()
    message_display = [['.' for x in range(100)] for y in range(100)]

    for x in range(1, 386):
        points_tracker[x] = {'x-position': 0, 'y-position': 0, 'velocity': (0,0)}

    point_number = 1

    with open('input.txt') as input_file:
        for line in input_file:
            line = line.replace(' ', '')
            data = line.split('=')
            initial_position = data[1].replace('<', '').split('>')[0].split(',')
            velocity = data[2].replace('<', '').replace('>', '').split(',')
            points_tracker[point_number]['x-position'] = int(initial_position[0]) + 10
            points_tracker[point_number]['y-position'] = int(initial_position[1]) + 10
            points_tracker[point_number]['velocity'] = (int(velocity[0]), int(velocity[1]))
            point_number += 1
    
    num_seconds = 1
    while num_seconds < 10559:
        for key in points_tracker:
            points_tracker[key]['x-position'] += points_tracker[key]['velocity'][0]
            points_tracker[key]['y-position'] += points_tracker[key]['velocity'][1]
            # message_display[points_tracker[key]['y-position']][points_tracker[key]['x-position']] = '#'

        # print(num_seconds)
        # pprint.pprint(points_tracker)

        # with open('message_display.txt', 'a') as f:
        #     print(num_seconds, file=f)
        #     for line in message_display:
        #         print(line, file=f)
        
        # message_display = [['.' for x in range(-20, 20)] for y in range(-20, 20)]

        num_seconds += 1

    for key in points_tracker:
        points_tracker[key]['x-position'] -= 150
        points_tracker[key]['y-position'] -= 180

    for key in points_tracker:
        message_display[points_tracker[key]['y-position']][points_tracker[key]['x-position']] = '#'

    with open('message_display.txt', 'a') as f:
            print(num_seconds, file=f)
            for line in message_display:
                print(line, file=f)

    pprint.pprint(points_tracker)

    # pprint.pprint(points_tracker)
    # with open('message_display.txt', 'a') as f:
    #     for line in message_display:
    #         print(line, file=f)
    
    # pprint.pprint(message_display)
            


if __name__ == "__main__":
    main()