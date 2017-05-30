import parcial_ej2
import unittest

extensiones = ["txt", "TXT", "doc", "DOC", "pdf", "PDF", "rtf", "RTF",
               "jpg", "JPG", "bmp", "BMP", "gif", "GIF", "png", "PNG",
               "wav", "WAV", "ogg", "OGG", "mp3", "MP3", "mp4", "MP4",
               "mpeg", "MPEG", "avi", "AVI", "py", "PY", "db", "DB",
               "js", "JS", "dll", "DLL", "iso", "ISO", "exe", "EXE"]

class testparcial_ej2(unittest.TestCase):

    def test_validar_extension_contrasta_extensiones_con_extension_en_minuscula_Devuelve_True(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.txt", extensiones))

    def test_validar_extension_contrasta_extensiones_con_extension_que_presenta_2mayusculas_y_1minuscula_Devuelve_True(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.tXt", extensiones))

    def test_validar_extension_contrasta_extensiones_con_extension_en_mayuscula_Devuelve_True(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.TXT", extensiones))

    def test_validar_extension_contrasta_extensiones_con_extension_que_presenta_1mayuscula_y_2minusculas_Devuelve_True(self):
        self.assertTrue(parcial_ej2.validar_extension("/usuario/m/m.TxT", extensiones))

    def test_validar_extension_contrasta_extensiones_con_archivo_sin_extension_Devuelve_False(self):
        self.assertFalse(parcial_ej2.validar_extension("/usuario/m/m.", extensiones))

    def test_validar_extension_contrasta_extensiones_con_ruta_sin_archivo_Devuelve_False(self):
        self.assertFalse(parcial_ej2.validar_extension("/usuario/m/", extensiones))

    def test_extension_contrasta_extensiones_con_nada_Devuelve_False(self):
        self.assertFalse(parcial_ej2.validar_extension("", extensiones))

    def test_extension_prueba_si_la_funcion_devuelve_una_lista_Devuelve_Falso(self):
        self.assertNotIsInstance((parcial_ej2.validar_extension("/usuario/m/m.TXT", extensiones)), list)

    def test_extension_prueba_si_la_funcion_devuelve_un_str_Devuelve_Falso(self):
        self.assertNotIsInstance( (parcial_ej2.validar_extension("/usuario/m/m.TXT", extensiones)), str)

    def test_extension_prueba_si_la_funcion_devuelve_un_float_Devuelve_Falso(self):
        self.assertNotIsInstance( (parcial_ej2.validar_extension("/usuario/m/m.TXT", extensiones)), float)