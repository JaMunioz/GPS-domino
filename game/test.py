"""
AQUI SE REALIZARAN LOS TEST AL DOMINO
"""

# Creating tests for domino_refactored.py

import unittest
from unittest.mock import patch
from domino import parse_players
from begin_logic import repartir_fichas, determinar_jugador_inicial


class TestDomino(unittest.TestCase):
    def test_repartir_fichas_2(self):
        repartidas = 14
        players = 2
        with patch("builtins.input", side_effect=[players]):
            for i in range(players):
                self.assertEqual(len(repartir_fichas(players)[f"j{i+1}"]), repartidas)

    def test_repartir_fichas_3(self):
        repartidas = 9
        players = 3
        with patch("builtins.input", side_effect=[players]):
            for i in range(players):
                self.assertEqual(len(repartir_fichas(players)[f"j{i+1}"]), repartidas)

    def test_repartir_fichas_14(self):
        repartidas = 2
        players = 14
        with patch("builtins.input", side_effect=[players]):
            for i in range(players):
                self.assertEqual(len(repartir_fichas(players)[f"j{i+1}"]), repartidas)

    def test_parse_players_ABC(self):
        value = "ABC"
        with patch("builtins.input", side_effect=[value, "8"]):
            self.assertEqual(parse_players(value), 8)

    def test_parse_players_1(self):
        value = "1"
        with patch("builtins.input", side_effect=[value, "2"]):
            self.assertEqual(parse_players(value), 2)

    def test_parse_players_15(self):
        value = "15"
        with patch("builtins.input", side_effect=[value, "4"]):
            self.assertEqual(parse_players(value), 4)

    def test_parse_players_0(self):
        value = "0"
        with patch("builtins.input", side_effect=[value, "3"]):
            self.assertEqual(parse_players(value), 3)

    def test_parse_players_minus_5(self):
        value = "-5"
        with patch("builtins.input", side_effect=[value, "5"]):
            self.assertEqual(parse_players(value), 5)

    def test_determinar_jugador_inicial_66(self):
        fichas = {
            "j1": [[2, 2], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[5, 5], [1, 2]],
            "j4": [[6, 6], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }

        self.assertEqual(determinar_jugador_inicial(fichas), "j4")

    def test_determinar_jugador_inicial_55(self):
        fichas = {
            "j1": [[4, 4], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[5, 5], [1, 2]],
            "j4": [[2, 3], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }
        self.assertEqual(determinar_jugador_inicial(fichas), "j3")

    def test_determinar_jugador_inicial_44(self):
        fichas = {
            "j1": [[4, 4], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[6, 2], [1, 2]],
            "j4": [[2, 2], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }
        self.assertEqual(determinar_jugador_inicial(fichas), "j1")

    def test_determinar_jugador_inicial_33(self):
        fichas = {
            "j1": [[6, 5], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[3, 3], [1, 2]],
            "j4": [[2, 2], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }

        self.assertEqual(determinar_jugador_inicial(fichas), "j3")

    def test_determinar_jugador_inicial_22(self):
        fichas = {
            "j1": [[6, 5], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[2, 5], [1, 2]],
            "j4": [[2, 2], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }

        self.assertEqual(determinar_jugador_inicial(fichas), "j4")

    def test_determinar_jugador_inicial_11(self):
        fichas = {
            "j1": [[6, 5], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[2, 5], [1, 2]],
            "j4": [[1, 1], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }

        self.assertEqual(determinar_jugador_inicial(fichas), "j4")

    def test_determinar_jugador_inicial_00(self):
        fichas = {
            "j1": [[6, 5], [2, 4]],
            "j2": [[1, 5], [0, 2]],
            "j3": [[2, 5], [1, 2]],
            "j4": [[0, 1], [0, 0]],
            "j5": [[0, 4], [1, 6]],
        }

        self.assertEqual(determinar_jugador_inicial(fichas), "j4")

    def test_determinar_jugador_inicial_sin_chancho(self):
        fichas = {
            "j1": [[0, 5], [1, 6]],
            "j2": [[1, 6], [3, 4]],
            "j3": [[3, 4], [0, 2]],
            "j4": [[0, 2], [2, 6]],
            "j5": [[2, 6], [1, 2]],
            "j6": [[1, 2], [2, 5]],
            "j7": [[2, 5], [1, 3]],
            "j8": [[1, 3], [0, 1]],
            "j9": [[0, 1], [3, 5]],
            "j10": [[3, 5], [2, 4]],
        }
        initial_player = determinar_jugador_inicial(fichas)
        self.assertIn(initial_player, fichas)


if __name__ == "__main__":
    unittest.main()


"Tests written and saved to test_refactored.py"
