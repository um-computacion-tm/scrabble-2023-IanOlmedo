from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]

    def validate_word_inside_board(self, word, location, orientation):
        row, col = location
        word_length = len(word)

        if orientation == "H":
            if col + word_length <= 15:
                return True
        elif orientation == "V":
            if row + word_length <= 15:
                return True

        return False


    def validate_word_out_of_board(self, word, location, orientation):
        return not self.validate_word_inside_board(word, location, orientation)


    