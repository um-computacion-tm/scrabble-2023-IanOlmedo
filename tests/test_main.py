from main import Main
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from game.scrabble import Scrabble

"""class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['3'])   
    def test_valid_player_count(self,mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)

    @patch('builtins.input', side_effect=['3'])
    def test_valid_player_count_error(self, mock_input):
        main = Main()
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)

    @patch('builtins.input', side_effect=['3']) 
    def test_player_count_input_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)
    
    @patch('builtins.input', side_effect=['5', '3'])
    def test_player_count_input_invalid_then_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('Valor inválido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)

if __name__ == "__main__":
    unittest.main()"""

class TestScrabbleGame(unittest.TestCase):
    @patch('builtins.print')
    @patch('game.cli.show_player')
    @patch('game.cli.show_board')
    @patch('game.cli.get_player_count', return_value=3)
    @patch('game.cli.get_inputs', return_value=((1, 3), 'H', 'CASA'))
    @patch.object(Scrabble, 'is_playing', side_effect=[True, False])
    @patch.object(Scrabble, 'get_current_player', return_value=(0, "Player",))
    @patch.object(Scrabble, 'play')
    def test_main(self, *args):
        main()

if __name__ == '__main__':
    unittest.main()