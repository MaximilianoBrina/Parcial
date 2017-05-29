import parcial_ej2
import unittest

extensiones = ["txt", "TXT", "doc", "DOC", "pdf", "PDF", "rtf", "RTF",
               "jpg", "JPG", "bmp", "BMP", "gif", "GIF", "png", "PNG",
               "wav", "WAV", "ogg", "OGG", "mp3", "MP3", "mp4", "MP4",
               "mpeg", "MPEG", "avi", "AVI", "py", "PY", "db", "DB",
               "js", "JS", "dll", "DLL", "iso", "ISO", "exe", "EXE"]

class testparcial_ej2(unittest.TestCase):

    def test_True(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.txt",extensiones))

    def test_True2(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.tXt",extensiones))

    def test_True3(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.TXT",extensiones))

    def test_True4(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.TxT",extensiones))

    def test_Vacio(self):
        self.assertFalse(parcial_ej2.validar_extension("/usuario/m/m.",extensiones))

    def test_Vacio2(self):
        self.assertFalse(parcial_ej2.validar_extension("/usuario/m/",extensiones))

    def test_Vacio3(self):
        self.assertFalse(parcial_ej2.validar_extension("",extensiones))

    def test_Tipo(self):
        self.assertNotIsInstance( (parcial_ej2.validar_extension("/usuario/m/m.TXT",extensiones)), list)

    def test_Tipo2(self):
        self.assertNotIsInstance( (parcial_ej2.validar_extension("/usuario/m/m.TXT",extensiones)), str)

    def test_Tipo2(self):
        self.assertNotIsInstance( (parcial_ej2.validar_extension("/usuario/m/m.TXT",extensiones)), float)