import parcial_ej3
import unittest

class testparcial_ej3(unittest.TestCase):

    def test_generador_matriz_triangular_comprueba_que_la_funcion_genera_una_lista_Devuelve_True(self):
        self.assertIsInstance(parcial_ej3.generador_matriz_triangular(3), list)

    def test_generador_matriz_triangular_comprueba_que_la_extension_de_la_matriz_sea_igual_al_numero_ingresado(self):
        self.assertEqual(len(list(parcial_ej3.generador_matriz_triangular(2))), 2)

    def test_generador_matriz_triangular_comprueba_que_la_extension_de_la_matriz_devuelve_0_si_se_ingresa_un_str(self):
        self.assertEqual(len(list(parcial_ej3.generador_matriz_triangular("Rosita"))), 0)

    def test_generador_matriz_triangular_comprueba_el_ingreso_de_un_str_devuelve_false(self):
        self.assertFalse(parcial_ej3.generador_matriz_triangular("Rosita"))

    def test_generador_matriz_triangular_comprueba_que_devuelve_False_si_se_ingresa_un_numero_negativo(self):
        self.assertFalse(parcial_ej3.generador_matriz_triangular(-2))
