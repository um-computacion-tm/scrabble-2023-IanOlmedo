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

    def playing(self):
        return True
    """
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player==self.players[-1]: #accediendo al ultimo valor de la lista

            index = (0)
            self.players.index(self.current_player)+1
            self.current_player = self.players[index]

    def validate_word(self,word,location,orientation):
        #1-validar que el user tiene las letras
        #2-que la palabra etre en el tablero
        self.board.validate

    def get_words():
        #obtener las posibles palabras que se pueden formar , dad una palabra, ubicada
        #preguntar al usuario, por cada una de las palabras, las que considera como correcta
"""
