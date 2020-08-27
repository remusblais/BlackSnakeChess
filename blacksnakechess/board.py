from position import Position
from piece import Piece

class Board:

    def __init__(self, rows, columns):
        self.x_spaces = columns
        self.y_spaces = rows

        self.spaces = {
            Position(7, 0): Piece('white', 'rook'),
            Position(7, 1): Piece('white', 'bishop'),
            Position(7, 2): Piece('white', 'knight'),
            Position(7, 3): Piece('white', 'queen'),
            Position(7, 4): Piece('white', 'king'),
            Position(7, 5): Piece('white', 'knight'),
            Position(7, 6): Piece('white', 'bishop'),
            Position(7, 7): Piece('white', 'rook'),
            Position(6, 0): Piece('white', 'pawn'),
            Position(6, 1): Piece('white', 'pawn'),
            Position(6, 2): Piece('white', 'pawn'),
            Position(6, 3): Piece('white', 'pawn'),
            Position(6, 4): Piece('white', 'pawn'),
            Position(6, 5): Piece('white', 'pawn'),
            Position(6, 6): Piece('white', 'pawn'),
            Position(6, 7): Piece('white', 'pawn'),
            Position(0, 0): Piece('black', 'rook'),
            Position(0, 1): Piece('black', 'bishop'),
            Position(0, 2): Piece('black', 'knight'),
            Position(0, 3): Piece('black', 'queen'),
            Position(0, 4): Piece('black', 'king'),
            Position(0, 5): Piece('black', 'knight'),
            Position(0, 6): Piece('black', 'bishop'),
            Position(0, 7): Piece('black', 'rook'),
            Position(1, 0): Piece('black', 'pawn'),
            Position(1, 1): Piece('black', 'pawn'),
            Position(1, 2): Piece('black', 'pawn'),
            Position(1, 3): Piece('black', 'pawn'),
            Position(1, 4): Piece('black', 'pawn'),
            Position(1, 5): Piece('black', 'pawn'),
            Position(1, 6): Piece('black', 'pawn'),
            Position(1, 7): Piece('black', 'pawn'),
        }

    def __repr__(self):
        """ Showcase the entire boardgame grid """

        hor_bar = '\u2500'  # ─
        ver_bar = '\u2502'  # │
        cross_bar = '\u253c'  # ┼

        boardgame = f' {cross_bar}'
        for num in range(self.x_spaces):
            boardgame += f'{hor_bar}{str(num)}{hor_bar}{cross_bar}'
        boardgame += '\n'

        for x in range(self.y_spaces):
            row_separator = f'{hor_bar * 3}{cross_bar}'
            boardgame += f'{str(x)}{ver_bar} '
            for y in range(self.x_spaces):
                if Position(x, y) in self.spaces:
                    boardgame += str(self.spaces[Position(x, y)]) + " | "
                else:
                    boardgame += f'  {ver_bar} '
            boardgame += f'\n {cross_bar}{row_separator * self.x_spaces}\n'

        return boardgame




if __name__ == '__main__':
    new_board = Board(8, 8)
    print(new_board.__repr__())




