import unittest
from decimal import Decimal

from logica import UNIDADES, convertir, formatear, validar_edicion


class Conversiones(unittest.TestCase):
    def test_validacion_durante_edicion(self):
        for texto in ["", "-", "+", ".", ",", "-.", "12", "12,5", "12.5", "-2", "+3"]:
            self.assertTrue(validar_edicion(texto), texto)
        for texto in ["abc", "12a", "1,2.3", "1 000", "12%", "１２", "2\n3", "--2"]:
            self.assertFalse(validar_edicion(texto), texto)

    def test_incompletos_no_se_convierten(self):
        unidades = list(UNIDADES)
        for texto in ["-", "+", ".", ",", "-."]:
            with self.subTest(texto=texto), self.assertRaises(ValueError):
                convertir(texto, unidades[0], unidades[1])

    def test_formato(self):
        for numero, esperado in [("0", "0"), ("-0", "0"), ("12.500", "12,5"), ("1000", "1000"), ("-0.001", "-0,001")]:
            self.assertEqual(formatear(Decimal(numero)), esperado)

    def test_nueve_combinaciones(self):
        unidades = list(UNIDADES)
        esperados = [["1000", "100", "1"], ["10000", "1000", "10"], ["1000000", "100000", "1000"]]
        for i, origen in enumerate(unidades):
            for j, destino in enumerate(unidades):
                with self.subTest(origen=origen, destino=destino):
                    self.assertEqual(convertir("1000", origen, destino), Decimal(esperados[i][j]))

    def test_decimales_y_precision(self):
        u = list(UNIDADES)
        for texto, esperado in [("12,5", "0.0125"), ("12.5", "0.0125"), ("-2", "-0.002"), ("0", "0"), (".5", "0.0005")]:
            self.assertEqual(convertir(texto, u[0], u[2]), Decimal(esperado))
        self.assertEqual(formatear(convertir("123456789012345678901234567890.123", u[0], u[2])), "123456789012345678901234567,890123")

    def test_invalidos(self):
        u = list(UNIDADES)
        for texto in ["", " ", "abc", "1,2.3", "NaN", "inf", "1 000", "--2"]:
            with self.subTest(texto=texto), self.assertRaises(ValueError):
                convertir(texto, u[0], u[1])


if __name__ == "__main__":
    unittest.main()
