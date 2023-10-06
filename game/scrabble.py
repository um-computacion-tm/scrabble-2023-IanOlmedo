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

    def get_words(self, location, orientation):
        # Lógica para obtener las posibles palabras que se pueden formar en la ubicación y orientación proporcionadas
        # Agregar la generación de palabras según las reglas del juego
        return []  # Debe implementarse la lógica real aquí

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


