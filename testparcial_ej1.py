import parcial_ej1
import unittest

class testparcial_ej1(unittest.TestCase):

    def test_divisores_contrasta_lista_de_numeros_con_nada_Devuelve_lista_vacia(self):
        self.assertEqual(parcial_ej1.divisores("", [1, 2, 3]), [])

    def test_divisores_contrasta_lista_de_numeros_con_numero_negativo_Devuelve_lista_vacia(self):
        self.assertEqual(parcial_ej1.divisores(-1, [1, 2, 3]), [])

    def test_divisores_contrasta_lista_de_numeros_con_cero_Devuelve_lista_vacia(self):
        self.assertEqual(parcial_ej1.divisores(0, [1, 2, 3]), [])

    def test_divisores_contrasta_lista_vacia_con_cero_Devuelve_lista_vacia(self):
        self.assertEqual(parcial_ej1.divisores(0, []), [])

    def test_divisores_contrasta_lista_de_numeros_con_1_Devuelve_1(self):
        self.assertEqual(parcial_ej1.divisores(1, [1, 2, 5, 44]), [1])

    def test_divisores_contrasta_lista_de_numeros_positivos_y_negativos_con_2_Devuelve_1_y_menos_2(self):
        self.assertEqual(parcial_ej1.divisores(2, [1, -2, 3, 134]), [1, -2])

    def test_divisores_contrasta_lista_de_numeros_positivos_y_negativos_con_8_Devuelve_1_menos_4_y_2(self):
        self.assertEqual(parcial_ej1.divisores(8, [1, 7, 2, -4, 6, 9]), [1, 2, -4])

    def test_divisores_contrasta_lista_de_numeros_positivos_y_negativos_con_331_Devuelve_1_y_331(self):
        self.assertEqual(parcial_ej1.divisores(331, [1, 2, 3, 7, 147, 331, 518]), [1, 331])

    #####

    def test_divisores_contrasta_lista_de_numeros_positivos_y_negativos_con_0_Devuelve_Not_None(self):
        self.assertIsNotNone(parcial_ej1.divisores(0, [1, 2, 3, 4, 5]))

    def test_divisores_contrasta_lista_de_numeros_positivos_con_numero_negativo_Devuelve_una_lista(self):
        self.assertIsInstance(parcial_ej1.divisores(-2, [2, 3, 4, 5, 6, 7, 8, 9]), list)

    def test_divisores_contrasta_lista_de_numeros_con_numero_mayor_inpar_Devuelve_False(self):
        self.assertFalse(parcial_ej1.divisores(1003, [43, 7, 157]))

    def test_divisores_contrasta_lista_de_numeros_con_numero_mayor_par_Devuelve_False(self):
        self.assertFalse(parcial_ej1.divisores(1000, [44, 6, 930]))

    def test_divisores_contrasta_lista_de_numeros_con_numero_menor_Devuelve_lista_vacia(self):
        self.assertEqual(parcial_ej1.divisores(45, [677, 67]), [])