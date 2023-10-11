from game.scrabble import Scrabble

def show_player(player_name, player_score):
    print(f"Jugador: {player_name}")
    print(f"Puntuación: {player_score}")      ## <----revisar


def get_player_count():
    while True:
        try:
            player_count = int(input('Cantidad de jugadores (1-3): '))
            if 1 <= player_count <= 3:
                return player_count
            else:
                print('Por favor, ingrese un número entre 1 y 3.')
        except ValueError:
            print('Por favor, ingrese un número válido.')

def show_board(board):
    print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
    for row_index, row in enumerate(board.grid):
        print(
            str(row_index).rjust(2) +
            '| ' +
            ' '.join([repr(cell) for cell in row])
        )

class Main:
    @staticmethod
    def main():
        player_count = get_player_count()
        game = Scrabble(player_count)
        while game.is_playing():
            show_board(game.get_board())
            game.show_current_player()
            word, coords, orientation = get_inputs()
            try:
                game.play(word, coords, orientation)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    Main.main()





    
