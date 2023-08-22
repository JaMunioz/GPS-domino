from display import *
from begin_logic import *
from in_game_logic import *
from first_move import *

while True:
    cantidad_jugadores = int(input("Indique la cantidad de jugadores: "))
    if cantidad_jugadores > 1 and cantidad_jugadores < 15:
        break
    print("La cantidad no es valida")

"""
Descomente las siguientes 3 lineas, cuando begin_logic.py este completo, y 
orden_de_jugadores en in_game_logic.py este completado, ademas recuerde que
debe borrar las otras 2 siguientes del comentario que indica el FAKE DATA..
"""
#jugadores = repartir_fichas(cantidad_jugadores)
#jugador_inicial = determinar_jugador_inicial(jugadores)
#orden_de_jugadores = generar_lista_de_jugadores(jugador_inicial)
#FAKE DATA (Tengo mas que claro que la cantidad de fichas del fake data no son)
jugadores = {"j1":[[6,6],[1,3],[1,6]],"j2":[[4,4],[1,2],[5,6]],"j3":[[4,1],[6,2],[1,5]]}
orden_de_jugadores = ["j3","j1","j2"]

print()
fichas_jugadas = [] # es una lista donde estan toda la fila de fichas jugadas,
                    # se agregan las fichas al inicio, o final de la lista..
                    # recuerda que una ficha es lo siguiente: [nº1,nº2]
ganador = None
while True:
    for i in orden_de_jugadores:
        print(f"{jugando(i)}, esta jugando..")
        print("\nSu mano es la siguiente")
        mostrar_fichas(jugadores[i])
        if len(fichas_jugadas) == 0:
            ficha_a_jugar = elegir_chancho(jugadores[i])
            fichas_jugadas.append(ficha_a_jugar)
        else:
            ficha_a_jugar = elegir_ficha(fichas_jugadas, jugadores[i])
            if ficha_a_jugar != None:
                fichas_jugadas = jugar_ficha_al_mazo(fichas_jugadas, ficha_a_jugar)
        if ficha_a_jugar != None:
            print(f"Se jugó lo siguiente: {mostrar_fichas([ficha_a_jugar])}")
            jugadores[i].remove(ficha_a_jugar)
            if len(jugadores[i]) == 0:
                ganador = i
                break
        else:
            print("El jugador no tiene nada en la mano para jugar.")
        print("\nLas siguientes fichas estan en mesa..")
        mostrar_fichas(fichas_jugadas)
        siguiente_jugada()
    if ganador != None:
        break

print(f"\n¡El {jugando(ganador)} es el ganador de esta partida!")

