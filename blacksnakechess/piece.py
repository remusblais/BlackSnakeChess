class Piece:
    """Constructor for every piece

    """

    def __init__(self, color_of_piece, type_of_piece):

        self.color = color_of_piece
        self.type = type_of_piece


    def king(self):
        """Detect if the selected piece is king type

        Returns:
            (bool) : True if piece is king

        """
        return self.type == "king"

    def queen(self):
        """Detect if the selected piece is queen type

        Returns:
            (bool) : True if piece is queen

        """
        return self.type == "queen"

    def bishop(self):
        """Detect if the selected piece is bishop type

        Returns:
            (bool) : True if piece is bishop

        """
        return self.type == "bishop"

    def knight(self):
        """Detect if the selected piece is knight type

        Returns:
            (bool) : True if piece is knight

        """
        return self.type == "knight"

    def rook(self):
        """Detect if the selected piece is rook type

        Returns:
            (bool) : True if piece is rook

        """
        return self.type == "rook"

    def pawn(self):
        """Detect if the selected piece is pawn type

        Returns:
            (bool) : True is piece is pawn

        """
        return self.type == "pawn"

    def white(self):
        """Detect if the selected piece is white color

        Returns:
            (bool) : True if piece white

        """
        return self.color == "white"

    def black(self):
        """Detect if the selected piece is black color

        Returns:
            (bool) : True if piece is black

        """
        return self.color == "black"

    def promotion(self, piece):
        """Promote the current piece (eg. pawn to king)

        """
        self.type = piece

    def __repr__(self):
        """Print the piece

        """
        if self.white():

            if self.king():
                return 'k'

            elif self.queen():
                return'q'

            elif self.bishop():
                return 'b'

            elif self.knight():
                return 'n'

            elif self.rook():
                return 'r'

            else:
                return 'p'

        if self.black():
            if self.king():
                return 'K'

            elif self.queen():
                return 'Q'

            elif self.bishop():
                return 'B'

            elif self.knight():
                return 'N'

            elif self.rook():
                return 'R'

            else:
                return 'P'
