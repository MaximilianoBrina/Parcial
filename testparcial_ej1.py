import parcial_ej1
import unittest

class testparcial_ej1(unittest.TestCase):

    def test_pruebas1(self):
        self.assertEqual(parcial_ej1.divisores("",[1,2,3]), [])

    def test_igualdad2(self):
        self.assertEqual(parcial_ej1.divisores(-1,[1,2,3]), [])

    def test_igualdad3(self):
        self.assertEqual(parcial_ej1.divisores(0, [1, 2, 3]), [])

    def test_igualdad4(self):
        self.assertEqual(parcial_ej1.divisores(0, []), [])

    def test_igualdad5(self):
        self.assertEqual(parcial_ej1.divisores(1, [1,2]), [1])

    def test_igualdad6(self):
        self.assertEqual(parcial_ej1.divisores(2, [1, -2]), [1,-2])

    def test_igualdad7(self):
        self.assertEqual(parcial_ej1.divisores(8,[1,7,2,-4,6,9]), [1,2,-4])

    def test_igualdad8(self):
        self.assertEqual(parcial_ej1.divisores(331,[1,2,3,7,147,331,518]), [1,331])

    ########
    def test_NotNone(self):
        self.assertIsNotNone(parcial_ej1.divisores(0,[1,2,3,4,5]))

    def test_Lista(self):
        self.assertIsInstance(parcial_ej1.divisores(-2,[2,3,4,5,6,7,8,9]), list)

    def test_nros_impares(self):
        self.assertFalse(parcial_ej1.divisores(1003,[43,7,157]))

    def test_nros_pares(self):
        self.assertFalse(parcial_ej1.divisores(1000, [44, 6, 930]))

    def test_igualdad(self):
        self.assertEqual(parcial_ej1.divisores(45,[677,67]), [])