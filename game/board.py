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
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value

