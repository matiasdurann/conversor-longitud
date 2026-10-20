"""Interfaz local del conversor. Ejecutar: python app.py."""

import tkinter as tk
import customtkinter as ctk

from logica import UNIDADES, convertir, formatear, validar_edicion

VERSION = "1.3.0"
VACIO = "Aquí aparecerá el resultado"


class Conversor(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("dark")
        super().__init__()
        self.title("Conversor de longitud")
        self.geometry("600x620")
        self.minsize(440, 600)
        self.configure(fg_color="#14171d")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.cantidad = tk.StringVar()
        self.origen = tk.StringVar(value=next(iter(UNIDADES)))
        self.destino = tk.StringVar(value="Metros (m)")
        self.resultado = tk.StringVar(value=VACIO)
        self.error = tk.StringVar()

        marco = ctk.CTkFrame(self, fg_color="transparent")
        marco.grid(row=0, column=0, sticky="nsew", padx=24, pady=24)
        marco.grid_columnconfigure((0, 1), weight=1, uniform="botones")
        marco.grid_rowconfigure(7, weight=1)
        ctk.CTkLabel(marco, text="Conversor de longitud", font=("Segoe UI", 25, "bold"), text_color="#f1f5fb").grid(row=0, column=0, columnspan=2, sticky="w")
        ctk.CTkLabel(marco, text="Milímetros · Centímetros · Metros", text_color="#a5afc0").grid(row=1, column=0, columnspan=2, sticky="w", pady=(2, 24))
        ctk.CTkLabel(marco, text="Cantidad", font=("Segoe UI", 14), text_color="#d5dce8").grid(row=2, column=0, columnspan=2, sticky="w")
        self.entrada = ctk.CTkEntry(marco, textvariable=self.cantidad, height=64, font=("Segoe UI", 26), fg_color="#1e242e", border_color="#4b6385", text_color="#f1f5fb", corner_radius=10, validate="key", validatecommand=(self.register(self.validar_edicion), "%P"))
        self.entrada.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(4, 20))

        unidades = ctk.CTkFrame(marco, fg_color="transparent")
        unidades.grid(row=4, column=0, columnspan=2, sticky="ew")
        unidades.grid_columnconfigure((0, 2), weight=1, uniform="unidades")
        ctk.CTkLabel(unidades, text="De").grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(unidades, text="A").grid(row=0, column=2, sticky="w")
        self.selector_origen = ctk.CTkComboBox(unidades, variable=self.origen, values=list(UNIDADES), state="readonly", width=135, height=44, fg_color="#1e242e", border_color="#394353", button_color="#394353", button_hover_color="#4b6385", dropdown_fg_color="#1e242e", dropdown_hover_color="#304360", text_color="#f1f5fb", dropdown_text_color="#f1f5fb")
        self.selector_origen.grid(row=1, column=0, sticky="ew")
        self.boton_intercambiar = ctk.CTkButton(unidades, text="⇄", font=("Segoe UI", 20), width=42, height=44, fg_color="#26364e", hover_color="#36547c", text_color="#9ac2ff", command=self.intercambiar)
        self.boton_intercambiar.grid(row=1, column=1, padx=8)
        self.selector_destino = ctk.CTkComboBox(unidades, variable=self.destino, values=list(UNIDADES), state="readonly", width=135, height=44, fg_color="#1e242e", border_color="#394353", button_color="#394353", button_hover_color="#4b6385", dropdown_fg_color="#1e242e", dropdown_hover_color="#304360", text_color="#f1f5fb", dropdown_text_color="#f1f5fb")
        self.selector_destino.grid(row=1, column=2, sticky="ew")
        ctk.CTkLabel(unidades, text="Intercambiar: Alt+I", text_color="#a5afc0").grid(row=2, column=0, columnspan=3, pady=(4, 16))
        self.boton_convertir = ctk.CTkButton(marco, text="Convertir", font=("Segoe UI", 15, "bold"), height=48, fg_color="#2d6de0", hover_color="#245aba", text_color="#ffffff", corner_radius=10, command=self.calcular)
        self.boton_convertir.grid(row=5, column=0, sticky="ew", padx=(0, 6))
        self.boton_limpiar = ctk.CTkButton(marco, text="Limpiar", font=("Segoe UI", 15), height=48, fg_color="#262d38", hover_color="#354051", text_color="#d5dce8", corner_radius=10, command=self.limpiar)
        self.boton_limpiar.grid(row=5, column=1, sticky="ew", padx=(6, 0))
        self.aviso = ctk.CTkLabel(marco, textvariable=self.error, text_color="#ffaaa5", wraplength=350, justify="left", height=42)
        self.aviso.grid(row=6, column=0, columnspan=2, sticky="ew", pady=4)
        panel = ctk.CTkFrame(marco, fg_color="#1c283b", border_color="#304869", border_width=1, corner_radius=14)
        panel.grid(row=7, column=0, columnspan=2, sticky="nsew")
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(1, weight=1)
        ctk.CTkLabel(panel, text="RESULTADO", text_color="#9ac2ff", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", padx=20, pady=(16, 0))
        self.salida = ctk.CTkLabel(panel, textvariable=self.resultado, text_color="#f1f5fb", font=("Segoe UI", 16), wraplength=480, justify="left", anchor="w")
        self.salida.grid(row=1, column=0, sticky="nsew", padx=16, pady=(8, 16))
        panel.bind("<Configure>", lambda e: self.salida.configure(wraplength=max(100, e.width - 32)))
        self.bind("<Return>", lambda e: self.calcular())
        self.bind("<Escape>", lambda e: self.limpiar())
        self.bind("<Alt-i>", lambda e: self.intercambiar())
        self.bind("<Alt-I>", lambda e: self.intercambiar())
        for variable in (self.cantidad, self.origen, self.destino):
            variable.trace_add("write", self.invalidar)
        self.after(100, self.entrada.focus_set)

    def validar_edicion(self, propuesta):
        if validar_edicion(propuesta):
            return True
        self.error.set("Solo números y un separador decimal: coma o punto.")
        return False

    def invalidar(self, *_):
        self.resultado.set(VACIO)
        self.salida.configure(font=("Segoe UI", 16))
        self.error.set("")

    def calcular(self):
        try:
            valor = convertir(self.cantidad.get(), self.origen.get(), self.destino.get())
        except ValueError as exc:
            self.invalidar()
            self.error.set(str(exc))
            self.entrada.focus_set()
            return
        self.error.set("")
        self.salida.configure(font=("Segoe UI", 28, "bold"))
        self.resultado.set(f"{formatear(valor)} {UNIDADES[self.destino.get()][0]}")

    def intercambiar(self):
        origen, destino = self.origen.get(), self.destino.get()
        self.origen.set(destino)
        self.destino.set(origen)
        self.resultado.set("—")

    def limpiar(self):
        self.cantidad.set("")
        self.origen.set(next(iter(UNIDADES)))
        self.destino.set("Metros (m)")
        self.invalidar()
        self.entrada.focus_set()


if __name__ == "__main__":
    Conversor().mainloop()
