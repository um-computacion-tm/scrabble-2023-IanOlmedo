from game.models import Tile

class MockCell:
    def __init__(self, calculated_value):
        self.calculated_value = calculated_value #crea una instancia de celda ficticia

class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.board = None  

    @property
    def rack(self):
        return self.tiles

    def validate_word(self, word):
        word_letters = list(word)
        rack_letters = [tile.letter for tile in self.tiles]

        for letter in word_letters:
            if letter not in rack_letters:
                return False
            rack_letters.remove(letter)

        return True
    

    def pass_turn(self):
        pass



