import random

def generar_lista_de_jugadores(jn, cantidad_jugadores):
    lista_jugadores = [jn] 
    for i in range(1, cantidad_jugadores):
        jugador_numero = (int(jn[1:]) + i) % cantidad_jugadores
        if jugador_numero == 0:
            jugador_numero = cantidad_jugadores
        lista_jugadores.append("j" + str(jugador_numero))
    return lista_jugadores

def mostrar_fichas(fichas):
    for i in fichas:
        print(i, end=" ")


"""
Se espera que con la siguiente funcion, seleccione la ficha al azar de las
de las posibles a jugar..

ejemplos de inputs..
fichas_jugadas:   [[5,2],[2,6],[6,6],[6,3]]
mano_del_jugador: [[1,2], [5,6]]
"""
def puede_jugar(ficha, extremo):
    return ficha[0] == extremo or ficha[1] == extremo

def elegir_ficha(fichas_jugadas, mano_del_jugador):    
    extremo_izquierdo = fichas_jugadas[0][0]
    extremo_derecho = fichas_jugadas[-1][1]
    fichas_disponibles = [ficha for ficha in mano_del_jugador if puede_jugar(ficha, extremo_izquierdo) or puede_jugar(ficha, extremo_derecho)]
    if fichas_disponibles:
        ficha_elegida = random.choice(fichas_disponibles)
        return ficha_elegida
    else:
        return None


"""
Se espera que con la siguiente funcion, agregue a fichas por cada turno.

ejemplos de inputs..
fichas_jugadas:   [[3,2],[2,6],[6,6],[6,3]]
ficha_a_jugar: [5,6]
"""
def jugar_ficha_al_mazo(fichas_jugadas, ficha_a_jugar):
    if not fichas_jugadas:
        fichas_jugadas.append(ficha_a_jugar)
        return fichas_jugadas
    extremo_izquierdo = fichas_jugadas[0][0]
    extremo_derecho = fichas_jugadas[-1][1]
    if ficha_a_jugar[0] == extremo_derecho:
        fichas_jugadas.append(ficha_a_jugar)
    elif ficha_a_jugar[1] == extremo_izquierdo:
        fichas_jugadas.insert(0, ficha_a_jugar)
    elif ficha_a_jugar[1] == extremo_derecho:
        fichas_jugadas.append([ficha_a_jugar[1], ficha_a_jugar[0]])
    elif ficha_a_jugar[0] == extremo_izquierdo:
        fichas_jugadas.insert(0, [ficha_a_jugar[1], ficha_a_jugar[0]])
    
    return fichas_jugadas

    # "fichas_jugadas" si es una lista que si tiene "n" elementos, para cuando
    # llega al return, se retornada "fichas_jugadas" con "n+1" elementos.
    # lo importante de esta funcion es que se evalue si la ficha insertada
    # va al inicio o al final de la lista, y agregarla de manera adecuada
    # si por ejemplo las fichas jugadas son: [[6,6], [6,3]], y tengo para 
    # jugar un [4,3], la lista final quedaria asi.. [[6,6], [6,3], [3,4]]
