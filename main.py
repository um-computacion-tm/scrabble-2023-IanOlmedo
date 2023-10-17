from game.scrabble import Scrabble

def show_player(player_name, player_score):
    print(f"Jugador: {player_name}")
    print(f"Puntuación: {player_score}")

def get_inputs():
    while True:
        word = input("Ingrese la palabra que desea jugar: ").strip().upper()
        coords = input("Ingrese las coordenadas (Ejemplo: 'A1') donde desea colocar la palabra: ").strip().upper()
        orientation = input("Ingrese la orientación (H para horizontal, V para vertical): ").strip().upper()

        if len(coords) != 2 or not coords[0].isalpha() or not coords[1].isdigit():
            print("Coordenadas deben tener un formato válido, por ejemplo, 'A1'.")
            continue

        x, y = ord(coords[0]) - ord('A'), int(coords[1]) - 1

        if orientation not in ('H', 'V'):
            print("Orientación debe ser 'H' (horizontal) o 'V' (vertical).")
            continue

        return word, (x, y), orientation

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
            except game.scrabble.InvalidWordException as e:
                print(f"Error: {e}")
            except game.scrabble.InvalidPlaceWordException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

if __name__ == '__main__':
    Main.main()
