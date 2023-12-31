from game.scrabble import Scrabble

class Main:
    def __init__(self):
        print('Bienvenido')
        self.player_count = self.get_player_count()
        self.game = Scrabble(self.player_count)
    def valid_player_count(self,player_count):
        try:
            count = int(player_count)
            if 2 <= count <= 4:
                return True
        except ValueError:
            pass
        return False
    def get_player_count(self):
        while True:
            player_count = input('Cantidad de jugadores: ')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor inválido')
    
    def play(self):
        print(f'La cantidad de jugadores es: {self.player_count}')
        self.game.next_turn()
        print(f"Turno del jugador 1")


if __name__ == "__main__":
    main = Main()
    main.play()
    
