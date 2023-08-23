"""
Este documento no requiere de cambios
"""

import os
import platform


jn_to_string = {
    "j1": "Jugador 1",
    "j2": "Jugador 2",
    "j3": "Jugador 3",
    "j4": "Jugador 4",
    "j5": "Jugador 5",
    "j6": "Jugador 6",
    "j7": "Jugador 7",
    "j8": "Jugador 8",
    "j9": "Jugador 9",
    "j10": "Jugador 10",
    "j11": "Jugador 11",
    "j12": "Jugador 12",
    "j13": "Jugador 13",
    "j14": "Jugador 14",
}


def jugando(jn):
    return jn_to_string[jn]


def siguiente_jugada():
    print("\nPresiona una tecla para continuar...", end="", flush=True)
    if platform.system() == "Windows":
        os.system("pause >nul")
    else:
        os.system("/bin/bash -c 'read -s -n 1 -p \"\"'")
    print()
    print("\n")
