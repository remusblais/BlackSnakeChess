class Board:
    def __init__(self, x_cases, y_cases):
        self.x_cases = x_cases
        self.y_cases = y_cases

        self.cases = {
            (7, 0): 'o',
            (7, 2): 'o',
            (7, 4): 'o',
            (7, 6): 'o',
            (6, 1): 'o',
            (6, 3): 'o',
            (6, 5): 'o',
            (6, 7): 'o',
            (5, 0): 'o',
            (5, 2): 'o',
            (5, 4): 'o',
            (5, 6): 'o',
            (2, 1): 'x',
            (2, 3): 'x',
            (2, 5): 'x',
            (2, 7): 'x',
            (1, 0): 'x',
            (1, 2): 'x',
            (1, 4): 'x',
            (1, 6): 'x',
            (0, 1): 'x',
            (0, 3): 'x',
            (0, 5): 'x',
            (0, 7): 'x',
        }

    def __repr__(self):
        """ Showcase the entire boardgame grid """

        hor_bar = '\u2500'  # ─
        ver_bar = '\u2502'  # │
        cross_bar = '\u253c'  # ┼

        boardgame = f' {cross_bar}'
        for num in range(self.y_cases):
            boardgame += f'{hor_bar}{str(num)}{hor_bar}{cross_bar}'
        boardgame += '\n'

        for x in range(0, self.x_cases):
            row_separator = f'{hor_bar * 3}{cross_bar}'
            boardgame += f'{str(x)}{ver_bar} '
            for y in range(0, self.y_cases):
                if (x, y) in self.cases:
                    boardgame += str(self.cases[(x, y)])+" | "
                else:
                    boardgame += f'  {ver_bar} '
            boardgame += f'\n {cross_bar}{row_separator * self.y_cases}\n'

        return boardgame

if __name__ == '__main__':
    print(repr(Board(8, 8)))
