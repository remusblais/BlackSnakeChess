"""
This is the main module where all game logic between the player(s) and computer occur.

"""

__author__ = "Rémus Blais"
__version__ = "0.01"
__date__ = "2020-08-27"

from pyfiglet import Figlet
from board import Board
from position import Position


class Game:

    def __init__(self, game_mode, rows, columns, computer=False, difficulty=1):
        """Game constructor

           Attributes:
               board (Board): Initialize the boardgame with pieces
               game_mode (int): Type of checkers game
               rows (int): Number of rows
               columns (int): Number of columns
               computer (bool): Play against computer
               difficulty (int): Level of difficulty against computer

        """
        self.board = Board(rows, columns)
        self.game_mode = game_mode
        self.rows = rows
        self.columns = columns
        self.computer = computer
        self.difficulty = difficulty
        self.player = 1

    def start(self):
        """Game start here

        """
        print(Figlet(font='slant').renderText('Test'))
        self.turn(self.player)

    def turn(self, player):
        """Behaviour of player's turn

         """
        print(self.board)
        if 1 != 1:
            return self.victory(player)
        else:
            move_source = self.source()
            move_target = self.target()
            return self.turn(player)

    def source(self):
        """Ask the player which source piece to play

        """
        while True:
            pos_line = input("Source line : ")
            if pos_line.isdecimal() and int(pos_line) < self.rows:
                pos_col = input("Source column : ")
                if pos_col.isdecimal() and int(pos_col) < self.columns:
                    source = Position(int(pos_line), int(pos_col))
                    validation = (self.validate_source(source))
                    if not validation[0]:
                        print(validation[1])
                    else:
                        self.source_selected = source
                        break
                else:
                    print('wrong!!!')

        return source
    
    def validate_source(self, source):
        """Validate the selected source

        """
        return source, source
    
    def target(self):
        """Ask the player which target to play

        """
        while True:
            pos_line = input("Target line : ")
            if pos_line.isdecimal() and int(pos_line) < self.rows:
                pos_col = input("Target column : ")
                if pos_col.isdecimal() and int(pos_col) < self.columns:
                    target = Position(int(pos_line), int(pos_col))
                    validation = (self.validate_target(target))
                    if not validation[0]:
                        print(validation[1])
                    else:
                        self.source_selected = target
                        break
                else:
                    print('wrong!!!')

        return target
    
    def validate_target(self, target):
        """Validate the selected target

        """
        return target, target

    def victory(self, player):
        print(f'{player}, you are the winner!!')


if __name__ == "__main__":
    mode = ['1 - international',
           ]

    print(Figlet(font='slant').renderText('Black\nSnake\nChess') + __version__)
    #print(*mode, sep='\n')
    #game = Game(input('Select mode:\n'))
    new_game = Game(1, 8, 8, False, 1)
    new_game.start()
