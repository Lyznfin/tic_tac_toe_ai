from colorama import Fore

def create_board() -> list[list[int]]:
    return [[None for _ in range(3)] for _ in range(3)]

def get_move(board: list[list[int]]) -> tuple[int]:
    valid_coordinate = [0, 1, 2]
    while True:
        while True:
            x = int(input(f"Input of the x coordinate: "))
            if x not in valid_coordinate:
                print("Invalid coordinate")
            else:
                break
        while True:
            y = int(input(f"Input of the y coordinate: "))
            if y not in valid_coordinate:
                print("Invalid coordinate")
            else:
                break
        if not is_valid_move(board, (x, y)):
            print("Invalid move. Coordinate is occupied")
        else:
            break            
    return (x, y)

def make_move(board: list[list[int]], coordinate: tuple[int], player: str) -> list[list[int]]:    
    board[coordinate[0]][coordinate[1]] = player
    new_board = board
    return new_board

def is_valid_move(board: list[list[int]], coordinate: tuple[int]) -> bool:
    if board[coordinate[0]][coordinate[1]] is not None:
        return False
    return True

def get_winner(board: list[list[int]]) -> str | None:
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

def render(board: list[list[int]]) -> None:
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

def main():
    board = create_board()
    players = [("player_1", "O"), ("player_2", "X")]
    turn = 0
    while True:
        player = players[turn % 2]
        move = get_move(board)
        board = make_move(board, move, player[1])
        render(board)
        turn += 1
    board = make_move(create_board(), (0, 1), "O")
    board = make_move(board, (0, 2), "X")
    board = make_move(board, (0, 0), "O")
    render(board)
    move = get_move(board)
    board = make_move(board, move, "X")
    render(board)

if __name__ == "__main__":
    main()