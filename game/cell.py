from game.models import Tile

class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter: Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def is_empty(self):
        return self.letter is None

    def has_letter(self, letter):
        return self.letter and self.letter.letter == letter

    def apply_word_multiplier(self, word_multiplier):
        if self.multiplier_type == 'word':
            self.multiplier *= word_multiplier

    def apply_letter_multiplier(self, letter_multiplier):
        if self.multiplier_type == 'letter':
            self.multiplier *= letter_multiplier
