import parcial_ej4
import unittest

class testparcial_ej4(unittest.TestCase):

    def test_IgualA_a(self):
        self.assertEqual((parcial_ej4.torneo_liga([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)])), "a")

    def test_distinta_distribucion_tuplas(self):
        self.assertEqual((parcial_ej4.torneo_liga([("d",1,"a",9),("a",1,"c",1),("c",1,"b",1),("a",1,"b",-2)])), "a")

    def test_desorden_elementos_de_las_tuplas_A(self):
        self.assertEqual((parcial_ej4.torneo_liga([("a",9,"d",1),("c",1,"a",1),("b",1,"c",1),("b",-2,"a",1)])), "a")

    def test_desorden_elementos_de_las_tuplas_B(self):
        self.assertEqual((parcial_ej4.torneo_liga([("a","d",9,1),(1,1,"a","c"),(1,"c","b",1),("b",-2,"a",1)])), "a")

    def test_diccionario_x_tuplas(self):
        self.assertEqual((parcial_ej4.torneo_liga([{"a":1,"b":-2},{"a":1,"c":1},{"c":1,"b":1},{"d":1,"a":9}])), "a")

    def test_todo_en_una_lista(self):
        self.assertEqual((parcial_ej4.torneo_liga(["a",1,"b",-2,"a",1,"c",1,"c",1,"b",1,"d",1,"a",9])), "a")

