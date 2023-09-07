from game.scrabble import Scrabble

def main():
    print("bienvenido!")
    while True:
        try:
            players_count = int(input("ingrese cantidad de jugadores: "))
            if players_count <= 1or players_count > 4:
                raise ValueError
            else:
                break

        except ValueError:
            print("Valor invalido")

        scrabble_game = Scrabble(players_count=players_count)
        print("Cantidad de jugadores", len(scrabble_game.players))
        scrabble_game.next_turn()
        print("turno del jugador {scrabble.current_players.id}")
        word = input("Ingrese la palabra: ")
        location_x = input("Ingrese posicion X: ")
        location_y = input("Ingrese posicion Y: ")
        location =(location_x, location_y)
        orientation = input("Ingrese orientacion (V/H)")
        scrabble_game.validate_word