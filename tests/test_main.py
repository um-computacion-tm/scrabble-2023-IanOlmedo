import unittest
from unittest.mock import patch
from main import get_player_count, Main

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(
            get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(
            get_player_count(),
            3,
            )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        self.assertEqual(
            get_player_count(),
            2,
        )

    @patch('game.scrabble.Scrabble.is_playing', side_effect=[True, False])
    @patch('game.scrabble.Scrabble.get_current_player', return_value=(0, "Player",))
    @patch('game.scrabble.Scrabble.play')
    @patch('main.get_inputs', return_value=("CASA", (1, 3), 'H'))
    @patch('main.show_board')
    @patch('main.show_player')
    @patch('main.get_player_count', return_value=3)
    def test_main(self, *args):
        with patch('main.Main.main', return_value=None):
            Main.main()

if __name__ == '__main__':
    unittest.main()
