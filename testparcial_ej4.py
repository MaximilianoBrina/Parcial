import parcial_ej4
import unittest

class testparcial_ej4(unittest.TestCase):

    def test_torneo_liga_evalua_cuatro_tuplas_y_devuelve_ganador_A(self):
        self.assertEqual((parcial_ej4.torneo_liga([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)])), "a")

    def test_torneo_liga_cambia_distribucion_de_cuatro_tuplas_y_devuelve_ganador_A(self):
        self.assertEqual((parcial_ej4.torneo_liga([("d",1,"a",9),("a",1,"c",1),("c",1,"b",1),("a",1,"b",-2)])), "a")

    def test_torneo_liga_evalua_cuatro_tuplas_alterando_orden_de_pares_de_elementos_devuelve_ganador_A(self):
        self.assertEqual((parcial_ej4.torneo_liga([("a",9,"d",1),("c",1,"a",1),("b",1,"c",1),("b",-2,"a",1)])), "a")

"""
    revisar el codigo

    def test_torneo_liga_evalua_cuatro_tuplas_alterando_orden_de_todos_los_elementos_devuelve_fallo(self):
        self.assertFalse((parcial_ej4.torneo_liga([("a","d",9,1),(1,1,"a","c"),(1,"c","b",1),("b",-2,"a",1)])), a)

    def test_torneo_liga_evalua_diccionario_x_tuplas_devuelve_fallo(self):
        self.assertNotEqual((parcial_ej4.torneo_liga([{"a":1,"b":-2},{"a":1,"c":1},{"c":1,"b":1},{"d":1,"a":9}])), "a")

    def test_torneo_liga_evalua_todos_los_elementos_en_una_lista_devuelve_fallo(self):
        self.assertNotEqual((parcial_ej4.torneo_liga(["a",1,"b",-2,"a",1,"c",1,"c",1,"b",1,"d",1,"a",9])), "a")
"""




















