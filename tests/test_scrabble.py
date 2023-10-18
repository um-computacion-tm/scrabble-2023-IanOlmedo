import unittest
from game.scrabble import Scrabble
from game.scrabble import InvalidPlaceWordException, InvalidWordException

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = Scrabble(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_start_game(self):
        scrabble_game = Scrabble(players_count=2)
        game_started = scrabble_game.playing()
        self.assertTrue(game_started)
    
    def test_next_turn_when_game_is_starting(self):
        # Validar que al comienzo, el turno es del jugador 0
        scrabble_game = Scrabble(players_count=3)

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = Scrabble(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = Scrabble(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_validate_word_simple(self):
        # Prueba simple para validar_word
        scrabble_game = Scrabble(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]

        word = "HELLO"
        location = (7, 7)
        orientation = "H"

        with self.assertRaises(InvalidWordException):
            is_valid = scrabble_game.validate_word(word, location, orientation)

    def test_get_words_simple(self):
        # Prueba simple para get_words
        scrabble_game = Scrabble(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]

        location = (7, 7)
        orientation = "H"

        words = scrabble_game.get_words(location, orientation)

        self.assertIsNotNone(words)
        self.assertIsInstance(words, list)

if __name__ == '__main__':
    unittest.main()

        

