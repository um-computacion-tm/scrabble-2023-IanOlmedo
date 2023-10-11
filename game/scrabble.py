from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.calculate_word_value import CalculateWordValue
from game.dictionary import Dictionary
class InvalidWordException(Exception):
    pass
class InvalidPlaceWordException(Exception):
    pass

class Scrabble:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player("Laura"))
        self.turn = 0
        self.current_player = None

    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            index = 0
            self.current_player = self.players[index]
        else:
            current_index = self.players.index(self.current_player)
            next_index = (current_index + 1) % len(self.players)
            self.current_player = self.players[next_index]

    def validate_word(self, word, location, orientation):
        if not self.dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")

    def get_words(self, word, location, orientation):
        words = []  # Lista para almacenar las palabras válidas

        position_x, position_y = location
        word_length = len(word)

        if orientation == "H":
            for i in range(word_length):
                current_x, current_y = position_x + i, position_y
                current_tile = self.board.grid[current_x][current_y]

                # Verifica si hay una letra en la celda o si es una celda vacía
                if current_tile.letter is None:
                    # Obtén la palabra horizontal que se puede formar con esta celda vacía
                    horizontal_word = self.get_horizontal_word(current_x, current_y)
                    if len(horizontal_word) > 1:  # Debe tener al menos 2 letras
                        words.append(horizontal_word)
        elif orientation == "V":
            for i in range(word_length):
                current_x, current_y = position_x, position_y + i
                current_tile = self.board.grid[current_x][current_y]

                # Verifica si hay una letra en la celda o si es una celda vacía
                if current_tile.letter is None:
                    # Obtén la palabra vertical que se puede formar con esta celda vacía
                    vertical_word = self.get_vertical_word(current_x, current_y)
                    if len(vertical_word) > 1:  # Debe tener al menos 2 letras
                        words.append(vertical_word)

        return words


    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.calculate_words_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def calculate_words_value(self, word):
        cal = CalculateWordValue()
        return cal.calculate_word_value(word)
        
    def dict_validate_word(self, word):
        dict = Dictionary()
        return dict.verify_word(word)
