"""Acceso compatible; la interfaz se encuentra en app.py."""

from logica import UNIDADES, convertir, formatear

VERSION = "1.2.1"

def __getattr__(nombre):
    if nombre == "Conversor":
        from app import Conversor
        return Conversor
    raise AttributeError(nombre)

if __name__ == "__main__":
    from app import Conversor
    Conversor().mainloop()
