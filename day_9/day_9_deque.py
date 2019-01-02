from collections import deque, defaultdict

def main(): 
    players = None
    highest_marble_value = None
    with open('input.txt') as input_file:
        for line in input_file:
            data = line.split(';')
            players = int(data[0].split(' ')[0])
            highest_marble_value = int(data[1].split(' ')[5])

    player_final_scores = marble_game(highest_marble_value * 100, players)
    print(sorted(player_final_scores.items(), key=lambda k_v: k_v[1], reverse=True))


def marble_game(highest_marble_value, players):
    play_scores = defaultdict(int)
    marbles_played = deque([0, 1])
    curr_player = 2

    for marble in range(2, int(highest_marble_value) + 1):
        if marble % 23 == 0: 
            marbles_played.rotate(7)
            play_scores[curr_player] += marble + marbles_played.pop()
            marbles_played.rotate(-1)
        else:
            marbles_played.rotate(-1)
            marbles_played.append(marble)
        curr_player += 1
        if curr_player > players:
            curr_player = curr_player % players
    
    return play_scores

if __name__ == "__main__":
    main()