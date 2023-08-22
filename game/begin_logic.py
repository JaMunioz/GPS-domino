#Generar una lista de listas (matriz) con las 28 fichas posibles.
def generar_fichas():
    fichas = []
    for i in range(7):
        for j in range(i, 7):
            fichas.append([i, j])
    return fichas

#Se reparten las fichas a los "n" jugadores, Todo jugador posee la misma 
# cantidad de fichas, en caso de que sobren fichas quedan en el mazo base.
def repartir_fichas(n):
    #Diccionario con las fichas de cada jugador, cada llave del diccionario
    # sera: jn, siendo "n" el numero respectivo del jugador..  
    # EJEMPLO para un juego de 7 jugadores: 
    # { j1:[[1,3], [2,5], [3,4], [2,2]], ..., j7:[[1,2], ..., [6,6]] }
    jugadores = {}

    fichas = generar_fichas()
    for i in range(n):
        #En teoria se crearian las llaves de cada jugadore, recibiendo un valor
        #  una lista que es su mano.
        jugadores["j"+str(i+1)] = ... #[[1,3], [2,5], [3,4], [2,2]]
    ...
# La funcion "repartir_fichas(n):" retorna el diccionario final, con las fichas
# repartidas.

# Se recorrera el diccionario de jugadores con sus respectivas manos, 
# donde se determinara quien tiene el chancho mayor.
# siendo los siguientes los chanchos.. [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
def determinar_jugador_inicial():
    ...
    #return "j1", o "j2", ..., "jn"
    # Es decir, se retorna el string que representa a la llave del diccioanrio
    #  del jugador que comienza

# Como generar las fichas - Rafael P
"""
fichas = generar_fichas()
for ficha in fichas:
    print(ficha)
"""

