from game.board import Board
from game.player import Player
from game.models import BagTiles

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
        # Lógica para validar la palabra en la ubicación y orientación proporcionadas
        # Agregar la validación de las letras del jugador y si la palabra cabe en el tablero
        return True  # Debe implementarse la lógica real aquí

    def get_words(self, location, orientation):
        # Lógica para obtener las posibles palabras que se pueden formar en la ubicación y orientación proporcionadas
        # Agregar la generación de palabras según las reglas del juego
        return []  # Debe implementarse la lógica real aquí


