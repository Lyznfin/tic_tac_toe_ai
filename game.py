from colorama import Fore

def create_board() -> list[list[int]]:
    return [[None for _ in range(3)] for _ in range(3)]

def get_coordinate(coordinate) -> int:
    '''
    Get a valid individual coordinate
    '''
    valid_coordinate = [0, 1, 2]
    while True:
        value = input(f"Input of the {coordinate} coordinate: ")
        try:
            value = int(value)
            if value not in valid_coordinate:
                print("Invalid coordinate")
            else:
                return value
        except ValueError:
            print("Invalid input type")

def get_move(board: list[list[int]]) -> tuple[int]:
    '''
    Get a valid coordinate
    '''
    while True:
        x = get_coordinate("x")
        y = get_coordinate("y")
        if not is_valid_move(board, (x, y)):
            print("Invalid move. Coordinate is occupied")
        else:
            break
    return (x, y)

def make_move(board: list[list[int]], coordinate: tuple[int], player: str) -> list[list[int]]:
    '''
    For player to occupy a valid coordinate on the board
    '''
    board[coordinate[0]][coordinate[1]] = player
    new_board = board
    return new_board

def is_valid_move(board: list[list[int]], coordinate: tuple[int]) -> bool:
    '''
    Check if a coordinate on the board is already occupied
    '''
    if board[coordinate[0]][coordinate[1]] is not None:
        return False
    return True

def get_winner(board: list[list[int]]) -> str | None:
    '''
    Check if there is a winner by matching each line in the board by the winning lines
    '''
    winning_lines = [
        # row
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # column
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
        ]

    for line in winning_lines:
        board_lines = [board[x][y] for (x, y) in line]
        matching = set(board_lines)
        if matching == None:
            continue
        if len(matching) == 1:
            return matching.pop()
        
    return None

def is_draw(board: list[list[int]]) -> bool:
    '''
    Check if board is full
    '''
    for line in board:
        if None in line:
            return False
    return True

def render(board: list[list[int]]) -> None:
    '''
    Render the board into the terminal
    '''
    display_as = {
        None: " ",
        "O": Fore.BLUE + u"O" + Fore.RESET,
        "X": Fore.GREEN + u"X" + Fore.RESET,
    }
    lines = []
    print(" ------- ")
    for i in range(0, 3):
        line = '| '
        for j in range(0, 3):
            line += display_as[board[i][j]] + " "
        line += '|'
        lines.append(line)
    print("\n".join(lines))
    print(" ------- ")

def run() -> None:
    board = create_board()
    players = [("player 1", "O"), ("player 2", "X")]
    turn = 0
    while True:
        player = players[turn % 2]
        move = get_move(board)
        board = make_move(board, move, player[1])
        render(board)
        winner = get_winner(board)
        if winner != None:
            print(f"Congrats {player[0]}, you've win!")
            break
        if is_draw(board):
            print("The game is a draw!")
            break
        turn += 1