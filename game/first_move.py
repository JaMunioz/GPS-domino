"""
Se espera que con la siguiente funcion, seleccione la ficha que tiene condicion
de chancho que tenga mayor valor

ejemplos de inputs..
mano_del_jugador: [[1,2], [5,6], [6,6]]
"""
def elegir_chancho(mano_del_jugador):
    sum_chancho = 0
    ficha_elegida = None
    for ficha in mano_del_jugador:
        if len(set(ficha)) == 1:
            suma_ficha = sum(ficha)
            if suma_ficha > sum_chancho:
                sum_chancho = suma_ficha
                ficha_elegida = ficha
    return ficha_elegida
    # el return aqui devuelve la lista que representa la ficha que es mayor
    # chancho, ejemplo: [6, 6]