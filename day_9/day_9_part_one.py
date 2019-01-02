def main():
    data = []

    with open('input.txt') as input_file:
        for line in input_file:
            data = line.split(';')
    
    players = int(data[0].split(' ')[0])
    highest_marble_value = int(data[1].split(' ')[5])

    player_scores = dict()

    for x in range(1, int(players) + 1):
        player_scores[x] = 0

    marbles_played = [0, 1]
    curr_marble_pos = 1
    current_player = 2

    for marble in range(2, int(highest_marble_value) + 1):
        # print(current_player % len(player_scores))
        if marble % 23 == 0:
            player_to_add = 0
            if (current_player % len(player_scores)) == 0:
                player_to_add = players
            else:
                player_to_add = current_player % len(player_scores)
            player_scores[player_to_add] += marble
            player_scores[player_to_add] += marbles_played[curr_marble_pos - 7]
            curr_marble_pos -= 7
            if curr_marble_pos < 0:
                # print(curr_marble_pos)
                curr_marble_pos += len(marbles_played)
                # print(curr_marble_pos)
                # print(len(marbles_played))
            marbles_played.pop(curr_marble_pos)
            # print('Marble', marble)
            # print('Current marble pos', curr_marble_pos)
            # print('Marbles played', marbles_played)
        else:
            if curr_marble_pos == len(marbles_played) - 1:
                marbles_played.insert(1, marble)
            else:
                marbles_played.insert(curr_marble_pos + 2, marble)
            curr_marble_pos = marbles_played.index(marble)
        current_player += 1
        # print('Marble', marble)
        # print('Current marble pos', curr_marble_pos)
        # print('Marbles played', marbles_played)

    # print(marbles_played)
    # print(player_scores)

    print(sorted(player_scores.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    main()