import unittest
from game.board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):

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

    



"""
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
"""

if __name__ == '__main__':
    unittest.main()
    

""" def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (4, 5)  # Ubicación dentro del tablero
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)"""