from game.models import Tile
from game.cell import Cell  

class Board:
    def __init__(self):
        self.grid = [[Cell() for _ in range(15)] for _ in range(15)]  # Representa el tablero como una matriz de celdas
        self.generate_board()  # Inicializa el tablero con los multiplicadores

    def generate_board(self):
  
        multiplier_rules = {
            'DL': [1, 2, 3, 5, 7, 9, 11, 13],
            'TL': [0, 7, 14],
            'DW': [0, 7, 14],
            'TW': [1, 2, 3, 4, 5, 9, 10, 11, 12, 13],
        }
        
        # Tablero con celdas vacias
        self.grid = [[Cell() for _ in range(15)] for _ in range(15)]

        # Multiplicadores a las celdas
        for x in range(15):
            for y in range(15):
                
                if x in multiplier_rules['DL'] and y in multiplier_rules['DL']:
                    self.grid[x][y].multiplier_type = 'DL'
                elif x in multiplier_rules['TL'] and y in multiplier_rules['TL']:
                    self.grid[x][y].multiplier_type = 'TL'
                elif x in multiplier_rules['DW'] and y in multiplier_rules['DW']:
                    self.grid[x][y].multiplier_type = 'DW'
                elif x in multiplier_rules['TW'] and y in multiplier_rules['TW']:
                    self.grid[x][y].multiplier_type = 'TW'

        # Restaurar la casilla central, que siempre es DW (Doble Palabra)
        self.grid[7][7].multiplier_type = 'DW'


        word_multipliers = [
            (0, 0), (0, 7), (0, 14),
            (7, 0), (7, 14),
            (14, 0), (14, 7), (14, 14)
        ]

        for position in word_multipliers:
            x, y = position
            self.grid[x][y].multiplier_type = 'word'
            self.grid[x][y].multiplier = 2 if (x, y) != (7, 7) else 3 

   
        letter_multipliers = [
            (1, 1), (1, 13),
            (2, 2), (2, 12),
            (3, 3), (3, 11),
            (4, 4), (4, 10),
            (13, 1), (13, 13),
            (12, 2), (12, 12),
            (11, 3), (11, 11),
            (10, 4), (10, 10)
        ]

        for position in letter_multipliers:
            x, y = position
            self.grid[x][y].multiplier_type = 'letter'
            self.grid[x][y].multiplier = 2 if (x, y) != (7, 7) else 3  # Casilla central es TL, el resto son DL



    def validate_word_inside_board(self, word, location, orientation):
        position_x, position_y = location  #<--Cambiar nombre de variable para que sea mas facil de entender
        word_length = len(word)

        if orientation == "H":
            if position_y + word_length <= 15:
                return True
        elif orientation == "V":
            if position_x + word_length <= 15:
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

    def validate_word_place_board(self, word, location, orientation):
        position_x, position_y = location
        word_length = len(word)

        if not self.validate_word_inside_board(word, location, orientation):
            return False

        for i in range(word_length):
            if orientation == "H":
                current_tile = self.grid[position_x + i][position_y]
            elif orientation == "V":
                current_tile = self.grid[position_x][position_y + i]

            if current_tile.letter is not None:
                return False

        return True

    def put_words_board(self, word, location, orientation):
        position_x, position_y = location
        word_length = len(word)

        if not self.validate_word_place_board(word, location, orientation):
            return False

        for i in range(word_length):
            if orientation == "H":
                self.grid[position_x + i][position_y].add_letter(word[i])
            elif orientation == "V":
                self.grid[position_x][position_y + i].add_letter(word[i])

        return True
    
    def generate_row_string(self, row, positions, row_index):
        row_values = []

        for cell in row:
            if isinstance(cell, Tile) and cell.letter:
                row_values.append(cell.letter.letter)
            else:
                if isinstance(cell, Cell):
                    if cell.letter:
                        row_values.append(cell.letter.letter)
                    else:
                        if cell.multiplier_type == "DL":
                            row_values.append('2L')
                        elif cell.multiplier_type == "TL":
                            row_values.append('3L')
                        elif cell.multiplier_type == "DW":
                            row_values.append('2P')
                        elif cell.multiplier_type == "TW":
                            row_values.append('3P')
                else:
                    row_values.append('-')

        row_string = ' '.join(row_values)

        return row_string




























