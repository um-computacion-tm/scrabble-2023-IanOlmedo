import unittest
from game.cell import Cell
from game.models import Tile
from game.calculate_word_value import CalculateWordValue

class TestCalculateWordValue(unittest.TestCase):
    def test_calculate_word_value(self):
        word = [
            Cell(letter=Tile('C', 3), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 1)),
            Cell(letter=Tile('A', 1))
        ]
        value = CalculateWordValue.calculate_word_value(word)
        self.assertEqual(value, 9)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 3), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 1)),
            Cell(letter=Tile('A', 1))
        ]
        for cell in word:
            cell.active = True

        value = CalculateWordValue.calculate_word_value(word)
        self.assertEqual(value, 12)

    def test_with_word_multiplier_false_0(self):
        word = [
            Cell(letter=Tile('C', 3), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 1)),
            Cell(letter=Tile('A', 1))
        ]
        for cell in word:
            cell.active = False

        value = CalculateWordValue.calculate_word_value(word)
        self.assertEqual(value, 0)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 3), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 1)),
            Cell(letter=Tile('A', 1), multiplier=2, multiplier_type='word')
        ]
        value = CalculateWordValue.calculate_word_value(word)
        self.assertEqual(value, 18)

if __name__ == '__main__':
    unittest.main()
