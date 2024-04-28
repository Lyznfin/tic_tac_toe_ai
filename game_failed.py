# This ones kinda sucked
# Encountered error -> Leave -> Forgot about it -> Comeback to an indescribable errors
# Yeah, no. Im not fixing this, better start anew

import time
from colorama import Fore

class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.has_taken_turn: bool = True

class TikTakToe:
    def __init__(self, *, player_one: Player, player_two: Player) -> None:
        self.player_one: Player = player_one
        self.player_two: Player = player_two
        self.board = self.create_board()
        self.players_coordinate: dict = {
            player_one.name: [],
            player_two.name: []
        }

    def create_board(self) -> list[list[int]]:
        return [[0 for _ in range(3)] for _ in range(3)]
    
    def check_match(self, target_list):
        input_list = [[(0, 0), (0, 1), (0, 2)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(2, 0), (2, 1), (2, 2)],
                    [(0, 0), (1, 0), (2, 0)],
                    [(0, 1), (1, 1), (2, 1)],
                    [(0, 2), (1, 2), (2, 2)],
                    [(0, 0), (1, 1), (2, 2)]]
        for sublist in target_list:
            if all(item in input_list for item in sublist):
                return True
        return False

    def has_win(self) -> int:
        if self.check_match(self.players_coordinate[player_one.name]):
            return 1
        elif self.check_match(self.players_coordinate[player_two.name]):
            return 2
        else:
            return 0

    def fill_board(self, player: Player, coordinate: tuple[int]):
        self.board[coordinate[0]][coordinate[1]] = 1 if player.name == player_one.name else 2
        self.players_coordinate[player.name] += (coordinate)
    
    def take_turn(self, player: Player):
        valid_coordinate = [0, 1, 2]
        _x = int(input(f"{player.name}, please take your turn | x: "))
        if _x not in valid_coordinate:
            print("Invalid coordinate")
            return
        _y = int(input(f"{player.name}, please take your turn | y: "))
        if _y not in valid_coordinate:
            print("Invalid coordinate")
            return
        coordinate = (_x, _y)
        if coordinate in self.players_coordinate[player_one.name] or coordinate in self.players_coordinate[player_two.name]:
            print(f"{coordinate} is taken, please take another spot")
            return
        
        self.board[coordinate[0]][coordinate[1]] = 1 if player.name == player_one.name else 2
        self.players_coordinate[player.name] += coordinate
        player.has_taken_turn = not player.has_taken_turn

    def __render(self) -> None:
        display_as = {
            0: " ",
            1: Fore.WHITE + u"o",
            2: Fore.WHITE + u"x",
        }
        lines = []
        print("---------")
        for i in range(0, 3):
            line = '| '
            for j in range(0, 3):
                line += display_as[self.board[i][j]] + " "
            line += '|'
            lines.append(line)
        print("\n".join(lines))
        print("---------")

    def start(self):
        while True:
            self.__render()
            if player_one.has_taken_turn:
                self.take_turn(player_two)
                player_one.has_taken_turn = not player_one.has_taken_turn
            elif player_two.has_taken_turn:
                self.take_turn(player_one)
                player_two.has_taken_turn = not player_two.has_taken_turn
            match self.has_win():
                case 0:
                    pass
                case 1:
                    print(f"congratulation! {player_one.name}")
                    break
                case 2:
                    print(f"congratulation! {player_two.name}")
                    break
            time.sleep(0.1)

player_one = Player("David")
player_two = Player("Jones")

game = TikTakToe(player_one=player_one, player_two=player_two)
game.start()