# jn es el jugador de partida, puede ser
# "j1" o "j2" o... "jn" dependiendo el limite de jugadores.
def generar_lista_de_jugadores(jn):
    ...
    # el return es una lista, del respectivo orden de los jugadores.
    # ej: si son 7 jugadores, y comienza el tercero, la lista a retornar debera
    # ser: ["j3","j4","j5","j6","j7","j1","j2"] 




# se recibe una lista tipo: [[4, 1], [6, 2], [1, 5]]
def mostrar_fichas(fichas):
    print(fichas) #esta linea es temporal..
    # y se printea lo siguiente: [4;1] [6;2] [1;5]
    # no hay return..




"""
Se espera que con la siguiente funcion, seleccione la ficha al azar de las
de las posibles a jugar..

ejemplos de inputs..
fichas_jugadas:   [[5,2],[2,6],[6,6],[6,3]]
mano_del_jugador: [[1,2], [5,6]]
"""
def elegir_ficha(fichas_jugadas, mano_del_jugador):
    ...
    # el return aqui devuelve la lista que representa la ficha, ejemplo: [1, 2]
    # en caso de que no hay una ficha a para poder a jugar, retornar: None




"""
Se espera que con la siguiente funcion, agregue a fichas por cada turno.

ejemplos de inputs..
fichas_jugadas:   [[3,2],[2,6],[6,6],[6,3]]
ficha_a_jugar: [5,6]
"""
def jugar_ficha_al_mazo(fichas_jugadas, ficha_a_jugar):
    ...
    # "fichas_jugadas" si es una lista que si tiene "n" elementos, para cuando
    # llega al return, se retornada "fichas_jugadas" con "n+1" elementos.
    # lo importante de esta funcion es que se evalue si la ficha insertada
    # va al inicio o al final de la lista, y agregarla de manera adecuada
    # si por ejemplo las fichas jugadas son: [[6,6], [6,3]], y tengo para 
    # jugar un [4,3], la lista final quedaria asi.. [[6,6], [6,3], [3,4]]