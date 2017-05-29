import parcial_ej3
import unittest

class testparcial_ej3(unittest.TestCase):

    def test_Tipo(self):
        self.assertIsInstance(parcial_ej3.generador_matriz_triangular(3), list)

    def test_Igual(self):
        self.assertEqual(len(list(parcial_ej3.generador_matriz_triangular(2))), 2)

    def test_Rosita(self):
        self.assertEqual(len(list(parcial_ej3.generador_matriz_triangular("Rosita"))), 0)

    def test_False(self):
        self.assertFalse(parcial_ej3.generador_matriz_triangular("Rosita"))

#CUAL DE LOS DOS VALE?
    def test_Negativo(self):
        self.assertFalse(parcial_ej3.generador_matriz_triangular(-2))

    def test_Negativo2(self):
        self.assertTrue(parcial_ej3.generador_matriz_triangular(-2))
