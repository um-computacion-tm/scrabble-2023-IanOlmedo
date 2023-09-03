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
    
    def next_turn(self):
        self.turn += 1

