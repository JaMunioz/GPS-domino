import random


# Generar una lista de listas (matriz) con las 28 fichas posibles.
def generar_fichas():
    fichas = []
    for i in range(7):
        for j in range(i, 7):
            fichas.append([i, j])
    return fichas


# Se reparten las fichas a los "n" jugadores, Todo jugador posee la misma
# cantidad de fichas, en caso de que sobren fichas quedan en el mazo base.
def repartir_fichas(cantidad_jugadores):
    if cantidad_jugadores < 2 or cantidad_jugadores > 14:
        raise ValueError("La cantidad de jugadores debe estar entre 2 y 14.")

    fichas = generar_fichas()
    random.shuffle(fichas)

    mano_jugadores = {}
    fichas_por_jugador = len(fichas) // cantidad_jugadores

    for i in range(cantidad_jugadores):
        inicio = i * fichas_por_jugador
        fin = inicio + fichas_por_jugador
        mano_jugadores[f"j{i+1}"] = fichas[inicio:fin]

    return mano_jugadores


# Se recorrera el diccionario de jugadores con sus respectivas manos,
# donde se determinara quien tiene el chancho mayor.
# siendo los siguientes los chanchos.. [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
def determinar_jugador_inicial(jugadores_fichas):
    chancho_mas_alto = -1
    jugador_chancho_mayor = None

    for jugador, fichas in jugadores_fichas.items():
        for ficha in fichas:
            if ficha[0] == ficha[1] and ficha[0] > chancho_mas_alto:
                chancho_mas_alto = ficha[0]
                jugador_chancho_mayor = jugador

    if jugador_chancho_mayor is None:
        for jugador, fichas in jugadores_fichas.items():
            for ficha in fichas:
                if sum(ficha) > chancho_mas_alto:
                    chancho_mas_alto = sum(ficha)
                    jugador_chancho_mayor = jugador
    return jugador_chancho_mayor


"""
#Como repartir las fichas a los jugadores - Rafael P
cantidad_jugadores = 5
jugadores_fichas = repartir_fichas(cantidad_jugadores)

for jugador, fichas in jugadores_fichas.items():
    print(f"{jugador}: {fichas}")

# Llamada a la función para determinar el jugador que parte - Rafael P
jugador_parte = determinar_jugador_inicial(jugadores_fichas)
print(f"El jugador que parte es: {jugador_parte}")
"""
