from game.cell import Cell
from game.models import Tile

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]

    def validate_word_inside_board(self, word, location, orientation):
        position_x, position_y = location
        word_length = len(word)

        if orientation == "H":
            if position_x + word_length <= 15:
                return True
        elif orientation == "V":
            if position_y + word_length <= 15:
                return True

        return False

    def validate_word_out_of_board(self, word, location, orientation):
        row, col = location
        word_length = len(word)

        if orientation == "H":
            # Verificar si la última letra de la palabra está fuera del tablero
            if col + word_length > 15:
                return True
        elif orientation == "V":
            # Verificar si la última letra de la palabra está fuera del tablero
            if row + word_length > 15:
                return True

        return False

    @property
    def is_empty(self):
        # Verificar si el tablero está completamente vacío
        for row in self.grid:
            for cell in row:
                if not cell.is_empty():
                    return False
        return True

    @staticmethod
    def calculate_word_value(word: list[Tile]) -> int:
        value: int = 0
        for tile in word:
            value += tile.value
        return value
    
        # En la función validate_word_place_board en board.py
    def validate_word_place_board(self, word, location, orientation):
        position_x, position_y = location
        word_length = len(word)

        if orientation == "H":
            # Verificar si la palabra cabe horizontalmente en el tablero y no colisiona con letras existentes
            if position_x + word_length <= 15:
                for i in range(word_length):
                    if not self.grid[position_x + i][position_y].is_empty() and \
                    (self.grid[position_x + i][position_y].letter is None or self.grid[position_x + i][position_y].letter.letter != word[i].letter):
                        return False
                return True
        elif orientation == "V":
            # Verificar si la palabra cabe verticalmente en el tablero y no colisiona con letras existentes
            if position_y + word_length <= 15:
                for i in range(word_length):
                    if not self.grid[position_x][position_y + i].is_empty() and \
                    (self.grid[position_x][position_y + i].letter is None or self.grid[position_x][position_y + i].letter.letter != word[i].letter):
                        return False
                return True

        return False

    @property
    def is_empty(self):
        # Verificar si el tablero está completamente vacío
        for row in self.grid:
            for cell in row:
                if not cell.is_empty() or cell.letter is not None:
                    return False
        return True



















