"""Conversiones exactas, sin dependencia de la interfaz."""

import re
from decimal import Decimal

UNIDADES = {"Milímetros (mm)": ("mm", 0), "Centímetros (cm)": ("cm", 1), "Metros (m)": ("m", 3)}


def convertir(texto, origen, destino):
    """Convierte sin redondeos binarios, admitiendo coma o punto decimal."""
    texto = texto.strip()
    if not texto:
        raise ValueError("Introduce una cantidad para convertir.")
    if not re.fullmatch(r"[+-]?(?:[0-9]+(?:[.,][0-9]*)?|[.,][0-9]+)", texto):
        raise ValueError("Escribe un número válido, por ejemplo 12,5 o 12.5.")
    valor = Decimal(texto.replace(",", "."))
    signo, digitos, exponente = valor.as_tuple()
    desplazamiento = UNIDADES[origen][1] - UNIDADES[destino][1]
    return Decimal((signo, digitos, exponente + desplazamiento))


def formatear(valor):
    if valor == 0:
        return "0"
    texto = format(valor, "f")
    if "." in texto:
        texto = texto.rstrip("0").rstrip(".")
    return texto.replace(".", ",")


def validar_edicion(texto):
    """Permite estados intermedios mientras se escribe, no al convertir."""
    return re.fullmatch(r"[+-]?[0-9]*(?:[.,][0-9]*)?", texto) is not None
