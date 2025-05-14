import tkinter as tk
from tkinter import scrolledtext, messagebox
from lexer import lexer
from parser import run_parser
from afd import afd
import io
import sys

terminal_visible = True

def ejecutar_codigo():
    salida_texto.config(state='normal')
    code = texto_codigo.get("1.0", tk.END).strip()
    salida_texto.delete("1.0", tk.END)

    if not code:
        messagebox.showwarning("Advertencia", "El área de código está vacía.")
        return

    try:
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        lexer(code)
        run_parser(code)
        afd(code)

        salida = sys.stdout.getvalue()
        sys.stdout = old_stdout

        if salida.strip():
            salida_texto.insert(tk.END, salida)
        else:
            salida_texto.insert(tk.END, "No hubo salida del lexer ni del parser.")
        salida_texto.config(state='disabled')
    except Exception as e:
        salida_texto.config(state='normal')
        sys.stdout = old_stdout
        salida_texto.insert(tk.END, f"⚠️ Error al procesar el código:\n{e}")
        salida_texto.config(state='disabled')

def limpiar_campos():
    salida_texto.config(state='normal')
    texto_codigo.delete("1.0", tk.END)
    salida_texto.delete("1.0", tk.END)
    salida_texto.config(state='disabled')
def toggle_terminal():
    global terminal_visible
    if terminal_visible:
        salida_label.pack_forget()
        salida_texto.pack_forget()
        boton_toggle_terminal.config(text="Mostrar Terminal")
    else:
        salida_label.pack(padx=10, pady=5, anchor="w")
        salida_texto.pack(padx=10, pady=(0, 10), expand=True, fill="both")
        boton_toggle_terminal.config(text="Ocultar Terminal")
    terminal_visible = not terminal_visible

# Crear ventana principal
ventana = tk.Tk()
ventana.title("ArduinoLite IDE")
ventana.geometry("800x600")

ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.columnconfigure(0, weight=1)

# === Fila superior: etiqueta + botones ===
top_frame = tk.Frame(ventana)
top_frame.pack(fill="x", padx=10, pady=5)

etiqueta = tk.Label(top_frame, text="Codigo:", font=("Arial",10, "bold"))
etiqueta.pack(side="left")

# Botones alineados a la derecha
botones_frame = tk.Frame(top_frame)
botones_frame.pack(side="right")

# Estilos comunes para botones
btn_base_style = {
    "bg": "white",
    "highlightthickness": 2,
    "highlightbackground": "black",
    "highlightcolor": "black",
    "font": ("Arial", 10, "bold"),
    "padx": 10,
    "pady": 3
}

boton_ejecutar = tk.Button(botones_frame, text="Ejecutar", command=ejecutar_codigo,
                           fg="green", **btn_base_style)
boton_ejecutar.pack(side="left", padx=5)

boton_limpiar = tk.Button(botones_frame, text="Limpiar", command=limpiar_campos,
                          fg="#5a7ca5", **btn_base_style)
boton_limpiar.pack(side="left", padx=5)

boton_toggle_terminal = tk.Button(botones_frame, text="Ocultar Terminal", command=toggle_terminal,
                                  fg="black", **btn_base_style)
boton_toggle_terminal.pack(side="left", padx=5)

# === Área de código ===
texto_codigo = scrolledtext.ScrolledText(ventana, font=("Consolas", 10, "italic bold"))
texto_codigo.pack(padx=10, pady=5, expand=True, fill="both")

# === Área de salida (terminal) ===
salida_label = tk.Label(ventana, text="Terminal:", font=("Arial", 10, "bold"))
salida_label.pack(padx=10, pady=5, anchor="w")

salida_texto = scrolledtext.ScrolledText(ventana, font=("Consolas", 10))
salida_texto.pack(padx=10, pady=(0, 10), expand=True, fill="both")
salida_texto.config(state='disabled')

ventana.mainloop()
