"""Esse arquivo testa o arquivo main.py"""

import unittest  # para criar o caso de teste

from main import target_sum


class TestMain(unittest.TestCase):
    """Classe para testar o main.py"""

    def test_target_sum_increasing(self):
        """Testa a função maior soma tudo crescente"""
        lista = [1, 2, 3, 4, 5]
        resultado_esperado = (4, 5)
        self.assertEqual(target_sum(lista, 9), resultado_esperado)

    def test_target_sum_decreasing(self):
        """Testa a função maior soma tudo decrescente"""
        lista = [5, 4, 3, 2, 1]
        resultado_esperado = (4, 5)
        self.assertEqual(target_sum(lista, 9), resultado_esperado)

    def test_target_sum_mixed(self):
        """Testa a função maior soma com números positivos e negativos"""
        lista = [10, -5, 20, 15, -30]
        resultado_esperado = (15, 20)
        self.assertEqual(target_sum(lista, 35), resultado_esperado)

    def test_target_sum_zeroes(self):
        """Testa a função maior soma com números 0 iguais"""
        lista = [0, 0, 0, 0]
        resultado_esperado = (0, 0)
        self.assertEqual(target_sum(lista, 0), resultado_esperado)

    def test_target_sum_negatives(self):
        """Testa a função maior soma com números negativos"""
        lista = [-10, -5, -2, -1]
        resultado_esperado = (-2, -1)
        self.assertEqual(target_sum(lista, -3), resultado_esperado)

    def test_target_sum_invalid(self):
        """Testa a função maior soma com entradas inválidas"""
        lista = [5]
        resultado_esperado = None
        self.assertEqual(target_sum(lista, 0), resultado_esperado)

        lista = []
        resultado_esperado = None
        self.assertEqual(target_sum(lista, 0), resultado_esperado)

        lista = [2, 3]
        resultado_esperado = None
        self.assertEqual(target_sum(lista, 10), resultado_esperado)
