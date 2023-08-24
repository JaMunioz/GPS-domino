from display import jugando, siguiente_jugada
from begin_logic import determinar_jugador_inicial, repartir_fichas
from begin_logic import ficha_mas_alta
from first_move import tiene_chancho
from in_game_logic import (
    elegir_ficha,
    mostrar_fichas,
    jugar_ficha_al_mazo,
    generar_lista_de_jugadores,
)
from first_move import elegir_chancho


def parse_players(cantidad_jugadores):
    while True:
        if not cantidad_jugadores.isdigit():  # check if the input is a number
            print("\nEntrada no válida. Por favor, ingrese un número.")
            print("\nIntente nuevamente.")
            cantidad_jugadores = input("Indique la cantidad de jugadores: ")
            continue

        cantidad_jugadores = int(cantidad_jugadores)
        if not (1 < cantidad_jugadores < 15):
            print("\nLa cantidad de jugadores debe estar entre 2 y 14.")
            print("\nIntente nuevamente.")
            cantidad_jugadores = input("Indique la cantidad de jugadores: ")
        else:
            break
    return cantidad_jugadores


def domino_game(cantidad_jugadores):
    jugadores = repartir_fichas(cantidad_jugadores)
    jugador_inicial = determinar_jugador_inicial(jugadores)
    orden_de_jugadores = generar_lista_de_jugadores(jugador_inicial, cantidad_jugadores)

    fichas_jugadas = []  # list of played domino pieces
    ganador = None
    es_empate = 0
    while True:
        for i in orden_de_jugadores:
            print(f"{jugando(i)}, esta jugando..")
            print("\nSu mano es la siguiente")
            mostrar_fichas(jugadores[i])
            if len(fichas_jugadas) == 0:
                if tiene_chancho(jugadores[i]):
                    ficha_a_jugar = elegir_chancho(jugadores[i])
                else:
                    ficha_a_jugar = ficha_mas_alta(jugadores[i])
                fichas_jugadas.append(ficha_a_jugar)

            else:
                ficha_a_jugar = elegir_ficha(fichas_jugadas, jugadores[i])
                if ficha_a_jugar is not None:
                    fichas_jugadas = jugar_ficha_al_mazo(fichas_jugadas, ficha_a_jugar)
            if ficha_a_jugar is not None:
                es_empate = 0
                print(f"Se jugó lo siguiente: {ficha_a_jugar}")
                jugadores[i].remove(ficha_a_jugar)
                if len(jugadores[i]) == 0:
                    ganador = i
                    break
            else:
                es_empate += 1
                print("El jugador no tiene nada en la mano para jugar.")
                if es_empate == cantidad_jugadores:
                    es_empate = True
                    break
            print("\nLas siguientes fichas estan en mesa..")
            mostrar_fichas(fichas_jugadas)
            siguiente_jugada()

        if ganador is not None:
            print(f"\n¡El {jugando(ganador)} es el ganador de esta partida!")
            break
        elif es_empate:
            print("\n¡Ningún jugador es el ganador de esta partida!")
            break


if __name__ == "__main__":
    user_input = input("Indique la cantidad de jugadores: ")
    cantidad_jugadores = parse_players(user_input)
    domino_game(cantidad_jugadores)
