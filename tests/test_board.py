import unittest
from game.board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertFalse(word_is_valid)

   # def test_board_is_empty(self):
        #board = Board()
        #self.assertTrue(board.is_empty)

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        self.assertFalse(board.is_empty)

    def test_validate_word_inside_board_horizontal_valid(self):
        board = Board()
        word = "Scrabble"
        location = (5, 5)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)

    def test_validate_word_inside_board_horizontal_invalid(self):
        board = Board()
        word = "Scrabble"
        location = (11, 5)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertFalse(word_is_valid)

    def test_validate_word_inside_board_vertical_valid(self):
        board = Board()
        word = "Scrabble"
        location = (5, 5)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)

    def test_validate_word_inside_board_vertical_invalid(self):
        board = Board()
        word = "Scrabble"
        location = (5, 11)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertFalse(word_is_valid)

    def test_validate_word_out_of_board_horizontal_valid(self):
        board = Board()
        word = "Scrabble"
        location = (9, 5)
        orientation = "H"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertFalse(word_is_valid) 

    def test_validate_word_out_of_board_horizontal_invalid(self):
        board = Board()
        word = "Scrabble"
        location = (11, 5)
        orientation = "H"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertFalse(word_is_valid)

    def test_validate_word_out_of_board_vertical_valid(self):
        board = Board()
        word = "Scrabble"
        location = (5, 9)
        orientation = "V"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertFalse(word_is_valid) 

    def test_validate_word_out_of_board_vertical_invalid(self):
        board = Board()
        word = "Scrabble"
        location = (5, 11)
        orientation = "V"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertFalse(word_is_valid)

    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (4, 5)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)

    def test_create_board_instance(self):
        board = Board()
        self.assertIsInstance(board, Board)

    def test_validate_word_out_of_board_horizontal_valid(self):
        board = Board()
        word = "Scrabble"
        location = (7, 9)
        orientation = "H"
        word_is_valid = board.validate_word_out_of_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_calculate_word_value_with_no_multiplier(self):
        board = Board()
        word = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 6)

    """def test_validate_word_place_board_horizontal_valid(self):
        board = Board()
        word = [
            Tile('F', 1), Tile('A', 1), Tile('C', 1), Tile('U', 1),
            Tile('L', 1), Tile('T', 1), Tile('A', 1), Tile('D', 1)
        ]
        location = (7, 4)  # Establece la ubicación adecuada
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_validate_word_place_board_vertical_collision(self):
        board = Board()
        # Eliminar las letras existentes en la ubicación de la prueba
        board.grid[5][5].add_letter(Tile('', 0))
        board.grid[5][6].add_letter(Tile('', 0))
        board.grid[5][7].add_letter(Tile('', 0))
        word = [
            Tile('S', 1), Tile('c', 3), Tile('r', 1), Tile('a', 2),
            Tile('b', 2), Tile('b', 2), Tile('l', 1), Tile('e', 1)
        ]
        location = (5, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertFalse(word_is_valid)"""


    def test_validate_word_place_board_horizontal_collision(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1))
        board.grid[9][7].add_letter(Tile('S', 1))
        board.grid[10][7].add_letter(Tile('A', 1))
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertFalse(word_is_valid)

    def test_validate_word_inside_board_horizontal_false(self):    ##########
        board = Board()
        word = "Scrabble"
        location = (12, 5)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertFalse(word_is_valid)


    def test_validate_word_out_of_board_horizontal_false(self):      ############
        board = Board()
        word = "Scrabble"
        location = (6, 5)
        orientation = "H"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertFalse(word_is_valid)

    def test_calculate_word_value_with_no_multiplier(self): ############
        board = Board()
        word = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        value = board.calculate_word_value(word) 
        self.assertEqual(value, 6)

    def test_validate_word_out_of_board_horizontal_false(self):
        board = Board()
        word = "Scrabble"
        location = (7, 12)  # Colocamos la palabra más allá del límite del tablero
        orientation = "H"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        self.assertTrue(word_is_valid)  # La palabra debería estar dentro del tablero

if __name__ == '__main__':
    unittest.main()

