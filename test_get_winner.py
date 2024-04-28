from main import get_winner
board_1 = [
  ['X', 'X', 'O'],
  ['O', 'X', None],
  ['O', 'O', 'X']
]
assert get_winner(board_1) == 'X', "return should be 'X'"
print(get_winner(board_1))

board_2 = [
  ['X', 'X', 'O'],
  ['O', None, 'X'],
  ['O', 'O', 'X']
]
assert get_winner(board_2) == None, "return should be 'None'"
print(get_winner(board_2))