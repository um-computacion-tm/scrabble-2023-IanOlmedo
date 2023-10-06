from game.scrabble import Scrabble

"""class Main:
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
    main.play()"""

def get_player_count():
    while True:
        try:
            player_count = int(input('cantidad de jugadores (1-3): '))
            if player_count <= 3:
                break
        except Exception as e:
            print('ingrese un numero por favor')

    return player_count

def show_board(board):
    print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
    for row_index, row in enumerate(board.grid):
        print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([repr(cell) for cell in row])
        )



def main():
    player_count = get_player_count()
    game = Scrabble(player_count)
    while game.is_playing():
        show_board(game.get_board())
        show_player(*game.get_current_player())
        word, coords, orientation = get_inputs()
        try:
            game.play(word, coords, orientation)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
    
