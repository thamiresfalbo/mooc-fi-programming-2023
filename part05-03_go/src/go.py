# Write your solution here
def who_won(game_board: list):
    player_one = 0
    player_two = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                player_one += 1
            elif game_board[i][j] == 2:
                player_two += 1

    if player_one == player_two:
        return 0
    elif player_one > player_two:
        return 1
    else:
        return 2
