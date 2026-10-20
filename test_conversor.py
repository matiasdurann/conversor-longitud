import unittest
from decimal import Decimal

from Conversor import Conversor, UNIDADES, convertir, formatear


class Conversiones(unittest.TestCase):
    def cerrar_ventana(self, app):
        # Evita callbacks pendientes de CustomTkinter entre ventanas de prueba.
        for identificador in app.tk.call("after", "info"):
            app.after_cancel(identificador)
        app.destroy()

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

    def test_botones(self):
        app = Conversor()
        app.withdraw()
        try:
            app.cantidad.set("1500")
            app.boton_convertir.invoke()
            self.assertEqual(app.resultado.get(), "1,5 m")
            app.cantidad.set("incorrecto")
            app.boton_convertir.invoke()
            self.assertTrue(app.error.get())
            app.boton_limpiar.invoke()
            self.assertEqual(app.cantidad.get(), "")
            self.assertEqual(app.error.get(), "")
            self.assertEqual(app.resultado.get(), "Aquí aparecerá el resultado")
            self.assertEqual(app.destino.get(), "Metros (m)")
            app.boton_intercambiar.invoke()
            self.assertEqual(app.origen.get(), "Metros (m)")
            self.assertEqual(app.destino.get(), next(iter(UNIDADES)))
            app.cantidad.set("1,25")
            app.boton_convertir.invoke()
            self.assertEqual(app.resultado.get(), "1250 mm")
            for _ in range(50):
                app.boton_intercambiar.invoke()
                app.boton_convertir.invoke()
                app.boton_limpiar.invoke()
            self.assertEqual(app.origen.get(), next(iter(UNIDADES)))
            self.assertEqual(app.destino.get(), "Metros (m)")
            self.assertEqual(app.cantidad.get(), "")
            for ancho, alto in [(440, 600), (600, 620), (900, 700)]:
                app.geometry(f"{ancho}x{alto}")
                app.update()
        finally:
            self.cerrar_ventana(app)

    def test_escritura_y_portapapeles(self):
        app = Conversor()
        try:
            app.update()
            for texto in ["abc", "12a", "1.2.3", "1,2.3", "1 000", "12%", "１２", "2\n3"]:
                app.boton_limpiar.invoke()
                app.entrada.insert(0, texto)
                self.assertEqual(app.cantidad.get(), "", texto)
                self.assertTrue(app.error.get())
                app.clipboard_clear()
                app.clipboard_append(texto)
                app.entrada._entry.event_generate("<<Paste>>")
                app.update()
                self.assertEqual(app.cantidad.get(), "", texto)
                app.boton_convertir.invoke()
                self.assertTrue(app.error.get())
            for texto in ["12", "12,5", "12.5", "-2", "+3", ".5"]:
                app.boton_limpiar.invoke()
                app.clipboard_clear()
                app.clipboard_append(texto)
                app.entrada._entry.event_generate("<<Paste>>")
                app.update()
                self.assertEqual(app.cantidad.get(), texto)
                app.boton_convertir.invoke()
                self.assertFalse(app.error.get())
            for texto in ["", "-", "+", ".", ",", "-."]:
                app.boton_limpiar.invoke()
                app.entrada.insert(0, texto)
                app.boton_convertir.invoke()
                self.assertTrue(app.error.get())
            app.boton_limpiar.invoke()
            app.cantidad.set("2")
            app.focus_force()
            app.update()
            app.event_generate("<Return>")
            app.update()
            self.assertEqual(app.resultado.get(), "0,002 m")
            app.event_generate("<Alt-i>")
            app.update()
            self.assertEqual(app.origen.get(), "Metros (m)")
            app.event_generate("<Escape>")
            app.update()
            self.assertEqual(app.cantidad.get(), "")
        finally:
            app.clipboard_clear()
            self.cerrar_ventana(app)


if __name__ == "__main__":
    unittest.main()
