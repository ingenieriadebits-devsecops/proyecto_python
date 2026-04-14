# ============================================
# Archivo: test_mychar.py
# Descripción: Pruebas unitarias para mychar.py
# Autor: Alumno D. José Luis Cabañas Cabañas
# Fecha: 27/10/2025
# Versión: 1.0
# ============================================

import unittest
from mychar import cadena_mas_larga

# Funciones de prueba para cadena_mas_larga
class TestCadenaMasLarga(unittest.TestCase):

    def test_caso_basico(self):
        self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "abcd")

    def test_lista_vacia(self):
        self.assertEqual(cadena_mas_larga([]), "")

    def test_cadenas_misma_longitud(self):
        self.assertEqual(cadena_mas_larga(["pera", "uva", "kiwi"]), "kiwi")

    def test_tipos_incorrectos(self):
        with self.assertRaises(TypeError):
            cadena_mas_larga("esto no es una lista")
    
    def test_elementos_no_cadena(self):
        with self.assertRaises(ValueError):
            cadena_mas_larga(["hola", 123, None])
    
    def test_caracteres_especiales(self):
        self.assertEqual(cadena_mas_larga(["áéíóú", "aeiouuu", "zzz"]), "aeiouuu")

if __name__ == "__main__":
    unittest.main()
