turn = 0
players = [("player_1", "O"), ("player_2", "X")]
while True:
    player = players[turn % 2]
    print(player[1])
    turn += 1
    if turn == 10:
        break