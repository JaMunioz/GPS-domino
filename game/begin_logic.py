import random

#Generar una lista de listas (matriz) con las 28 fichas posibles.
def generar_fichas():
    fichas = []
    for i in range(7):
        for j in range(i, 7):
            fichas.append([i, j])
    return fichas

#Se reparten las fichas a los "n" jugadores, Todo jugador posee la misma 
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
        mano_jugadores[f"Jugador {i+1}"] = fichas[inicio:fin]
    
    return mano_jugadores

# Se recorrera el diccionario de jugadores con sus respectivas manos, 
# donde se determinara quien tiene el chancho mayor.
# siendo los siguientes los chanchos.. [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
def determinar_jugador_inicial():
    ...
    #return "j1", o "j2", ..., "jn"
    # Es decir, se retorna el string que representa a la llave del diccioanrio
    #  del jugador que comienza


""" #Como generar las fichas - Rafael P
fichas = generar_fichas()
for ficha in fichas:
    print(ficha)
"""

"""#Como repartir las fichas a los jugadores - Rafael P
cantidad_jugadores = 5
jugadores_y_fichas = repartir_fichas(cantidad_jugadores)

for jugador, fichas in jugadores_y_fichas.items():
    print(f"{jugador}: {fichas}")
"""


