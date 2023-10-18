from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.calculate_word_value import CalculateWordValue
from game.dictionary import Dictionary
import sys
class InvalidWordException(Exception):
    pass
class InvalidPlaceWordException(Exception):
    pass
class InvalidPlayerCountException(Exception):
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

    def dict_validate_word(self, word):
        dict = Dictionary()
        return dict.verify_word(word)

    def validate_word(self, word, location, orientation):
        if not self.dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")

    def get_words(self, location, orientation):
        words = []  # Lista para almacenar las palabras válidas
        position_x, position_y = location

        if orientation == "H":
            for current_x in range(position_x, len(self.board.grid)):
                current_tile = self.board.grid[current_x][position_y]

                if current_tile.letter is None:
                    horizontal_word = self.get_horizontal_word(current_x, position_y)
                    if len(horizontal_word) > 1:
                        words.append(horizontal_word)
                    else:
                        break  # Rompe el bucle si no hay más celdas vacías en esta dirección
                else:
                    break  # Rompe el bucle si encuentra una letra

        elif orientation == "V":
            for current_y in range(position_y, len(self.board.grid[position_x])):
                current_tile = self.board.grid[position_x][current_y]

                if current_tile.letter is None:
                    vertical_word = self.get_vertical_word(position_x, current_y)
                    if len(vertical_word) > 1:
                        words.append(vertical_word)
                    else:
                        break  # Rompe el bucle si no hay más celdas vacías en esta dirección
                else:
                    break  # Rompe el bucle si encuentra una letra

        return words
    
    def get_horizontal_word(self, start_x, y):
        word = []
        x = start_x

        # Avanza hacia la izquierda para obtener las letras a la izquierda de la celda inicial
        while x >= 0 and self.board.grid[x][y].letter:
            word.insert(0, self.board.grid[x][y].letter.letter)
            x -= 1

        # Avanza hacia la derecha para obtener las letras a la derecha de la celda inicial
        x = start_x + 1
        while x < 15 and self.board.grid[x][y].letter:
            word.append(self.board.grid[x][y].letter.letter)
            x += 1

        return ''.join(word)


    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.calculate_words_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def calculate_words_value(self, word):
        cal = CalculateWordValue()
        return cal.calculate_word_value(word)

    def get_current_player(self):
        return self.players[self.turn]
    
    def is_playing(self):
        # El juego sigue en curso mientras haya fichas en la bolsa y haya al menos un jugador con fichas restantes.
        return not self.bag_tiles.is_empty() and any(player.has_tiles() for player in self.players)
    

    def get_player_count():
        while True:
            try:
                player_count = int(input('Cantidad de jugadores (2-4): '))
                if 2 <= player_count <= 4:
                    return player_count
                else:
                    print('Por favor, ingrese un número entre 2 y 4.')
                    raise InvalidPlayerCountException("Entrada incorrecta")
            except ValueError:
                print('Por favor, ingrese un número válido.')

    # En el código principal (main.py), puedes capturar la excepción así:
    try:
        player_count = get_player_count()
    except InvalidPlayerCountException as e:
        print(f"Error: {e}")

