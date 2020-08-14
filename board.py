class Board:
    def __init__(self, x_cases, y_cases):
        self.x_cases = x_cases
        self.y_cases = y_cases

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
                #if Position(x, y) in self.cases:
                #    boardgame += str(self.cases[Position(x, y)])+" | "
                #else:
                boardgame += f'  {ver_bar} '
            boardgame += f'\n {cross_bar}{row_separator * self.y_cases}\n'

        return boardgame

if __name__ == '__main__':
    print(repr(Board(6, 8)))
