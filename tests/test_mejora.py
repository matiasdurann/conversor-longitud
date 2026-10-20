"""Aceptación del intercambio usando el botón real de la interfaz."""

import unittest
from unittest.mock import patch

from app import Conversor
from logica import UNIDADES


class Intercambio(unittest.TestCase):
    def test_intercambio_conserva_texto_y_no_convierte(self):
        ventana = Conversor()
        ventana.withdraw()
        try:
            for origen in UNIDADES:
                for destino in UNIDADES:
                    for texto in ["0012,500", "+001.20", "-0,00", "", "-", "."]:
                        with self.subTest(origen=origen, destino=destino, texto=texto):
                            ventana.origen.set(origen)
                            ventana.destino.set(destino)
                            ventana.cantidad.set(texto)
                            ventana.resultado.set("resultado anterior")
                            with patch("app.convertir") as conversion:
                                ventana.boton_intercambiar.invoke()
                                self.assertEqual(ventana.origen.get(), destino)
                                self.assertEqual(ventana.destino.get(), origen)
                                self.assertEqual(ventana.cantidad.get(), texto)
                                self.assertEqual(ventana.resultado.get(), "—")
                                ventana.boton_intercambiar.invoke()
                                self.assertEqual(ventana.origen.get(), origen)
                                self.assertEqual(ventana.destino.get(), destino)
                                self.assertEqual(ventana.cantidad.get(), texto)
                                self.assertEqual(ventana.resultado.get(), "—")
                                conversion.assert_not_called()
            ventana.limpiar()
            ventana.cantidad.set("001,50")
            ventana.boton_convertir.invoke()
            self.assertEqual(ventana.resultado.get(), "0,0015 m")
            ventana.boton_intercambiar.invoke()
            self.assertEqual(ventana.resultado.get(), "—")
            ventana.boton_convertir.invoke()
            self.assertEqual(ventana.resultado.get(), "1500 mm")
            self.assertEqual(ventana.cantidad.get(), "001,50")
        finally:
            for identificador in ventana.tk.call("after", "info"):
                ventana.after_cancel(identificador)
            ventana.destroy()


if __name__ == "__main__":
    unittest.main()
