import unittest
from game.cell import Cell
from game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )

    def test_is_empty(self):
        empty_cell = Cell(multiplier=1, multiplier_type='letter')
        self.assertTrue(empty_cell.is_empty())

        non_empty_cell = Cell(multiplier=1, multiplier_type='letter')
        non_empty_cell.add_letter(Tile(letter='A', value=1))
        self.assertFalse(non_empty_cell.is_empty())

    def test_has_letter(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        cell.add_letter(Tile(letter='B', value=3))
        self.assertTrue(cell.has_letter('B'))
        self.assertFalse(cell.has_letter('A'))

    def test_apply_word_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        cell.apply_word_multiplier(3)
        self.assertEqual(cell.multiplier, 6)

        cell = Cell(multiplier=2, multiplier_type='letter')
        cell.apply_word_multiplier(3)
        self.assertEqual(cell.multiplier, 2)

    def test_apply_letter_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        cell.apply_letter_multiplier(3)
        self.assertEqual(cell.multiplier, 6)

        cell = Cell(multiplier=2, multiplier_type='word')
        cell.apply_letter_multiplier(3)
        self.assertEqual(cell.multiplier, 2)

    def test_add_player_starting_position(self):
        cell = Cell(multiplier=1, multiplier_type='')
        player = "Player 1"
        cell.add_player_starting_position(player)
        self.assertTrue(cell.is_starting_position)
        self.assertEqual(cell.player_starting_position, player)

    def test_inactive_cell(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        
        # Desactivamos la celda
        cell.active = False

        # La celda inactiva debe tener un valor de 0 independientemente de su contenido
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

if __name__ == '__main__':
    unittest.main()

