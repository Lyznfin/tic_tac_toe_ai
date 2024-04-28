import time
from colorama import Fore

def create_board() -> list[list[int]]:
    return [[None for _ in range(3)] for _ in range(3)]

def render(board) -> None:
    display_as = {
        None: " ",
        0: Fore.WHITE + u"o",
        1: Fore.WHITE + u"x",
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

render(create_board())