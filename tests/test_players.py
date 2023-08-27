import unittest
from game.models import Tile
from game.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player('Alice')
        self.assertEqual(player.name, 'Alice')
        self.assertEqual(len(player.tiles), 0)

    def test_rack_property(self):
        player = Player('Bob')
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        player.tiles = tiles
        self.assertEqual(player.rack, tiles)

    def test_validate_word_valid(self):
        player = Player('David')
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        self.assertTrue(player.validate_word('ABC'))


    def test_validate_word_invalid(self):
        player = Player('Eve')
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        self.assertFalse(player.validate_word('ABCD'))  

    def test_pass_turn(self):
        player = Player('Frank')
        player.pass_turn()  


class MockCell:
    def __init__(self, value):
        self.value = value

    def calculate_value(self): #simula el cálculo del valor de la celda. 
        return self.value


if __name__ == '__main__':
    unittest.main()
