class Board:
    def __init__(self, x_spaces, y_spaces):
        self.x_spaces = x_spaces
        self.y_spaces = y_spaces

        self.spaces = {
            (7, 0): 'T',
            (7, 1): 'F',
            (7, 2): 'B',
            (7, 3): 'Q',
            (7, 4): 'K',
            (7, 5): 'B',
            (7, 6): 'F',
            (7, 7): 'T',
            (6, 0): 'P',
            (6, 1): 'P',
            (6, 2): 'P',
            (6, 3): 'P',
            (6, 4): 'P',
            (6, 5): 'P',
            (6, 6): 'P',
            (6, 7): 'P',
            (0, 0): 't',
            (0, 1): 'f',
            (0, 2): 'b',
            (0, 3): 'k',
            (0, 4): 'q',
            (0, 5): 'b',
            (0, 6): 'f',
            (0, 7): 't',
            (1, 0): 'p',
            (1, 1): 'p',
            (1, 2): 'p',
            (1, 3): 'p',
            (1, 4): 'p',
            (1, 5): 'p',
            (1, 6): 'p',
            (1, 7): 'p',
        }

    def __repr__(self):
        """ Showcase the entire boardgame grid """

        hor_bar = '\u2500'  # ─
        ver_bar = '\u2502'  # │
        cross_bar = '\u253c'  # ┼

        boardgame = f' {cross_bar}'
        for num in range(self.y_spaces):
            boardgame += f'{hor_bar}{str(num)}{hor_bar}{cross_bar}'
        boardgame += '\n'

        for x in range(0, self.x_spaces):
            row_separator = f'{hor_bar * 3}{cross_bar}'
            boardgame += f'{str(x)}{ver_bar} '
            for y in range(0, self.y_spaces):
                if (x, y) in self.spaces:
                    boardgame += str(self.spaces[(x, y)])+" | "
                else:
                    boardgame += f'  {ver_bar} '
            boardgame += f'\n {cross_bar}{row_separator * self.y_spaces}\n'

        return boardgame

if __name__ == '__main__':
    print(repr(Board(8, 8)))
