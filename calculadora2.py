import tkinter as tk
from tkinter import ttk

def boton_clicado(valor):
    # Función que se ejecuta al hacer clic en un botón
    current = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, current + str(valor))

def calcular():
    # Función que se ejecuta al hacer clic en el botón "="
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="silver")

# Configuración de los estilos para los botones
estilo = ttk.Style()
estilo.configure("Estilo.TButton", font=("Arial", 16), background="silver", relief="raised")

# Configuración de la entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 20), justify=tk.RIGHT)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Configuración de los botones numéricos
botones_numericos = []
for i in range(9, 0, -1):
    fila = (9 - i) // 3 + 1
    columna = (9 - i) % 3
    boton = ttk.Button(ventana, text=str(i), style="Estilo.TButton")
    boton.configure(command=lambda x=i: boton_clicado(x))
    botones_numericos.append(boton)
    boton.grid(row=fila, column=columna, padx=5, pady=5)

# Configuración del botón "0"
boton_cero = ttk.Button(ventana, text="0", style="Estilo.TButton")
boton_cero.configure(command=lambda: boton_clicado(0))
boton_cero.grid(row=4, column=1, padx=5, pady=5)

# Configuración del botón de igual
boton_igual = ttk.Button(ventana, text="=", style="Estilo.TButton")
boton_igual.configure(command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

# Configuración de los botones de operaciones
boton_suma = ttk.Button(ventana, text="+", style="Estilo.TButton")
boton_suma.configure(command=lambda: boton_clicado('+'))
boton_suma.grid(row=1, column=3, padx=5, pady=5)

boton_resta = ttk.Button(ventana, text="-", style="Estilo.TButton")
boton_resta.configure(command=lambda: boton_clicado('-'))
boton_resta.grid(row=2, column=3, padx=5, pady=5)

boton_mult = ttk.Button(ventana, text="*", style="Estilo.TButton")
boton_mult.configure(command=lambda: boton_clicado('*'))
boton_mult.grid(row=3, column=3, padx=5, pady=5)

boton_div = ttk.Button(ventana, text="/", style="Estilo.TButton")
boton_div.configure(command=lambda: boton_clicado('/'))
boton_div.grid(row=4, column=3, padx=5, pady=5)

# Configuración del botón de limpiar
boton_limpiar = ttk.Button(ventana, text="C", style="Estilo.TButton")
boton_limpiar.configure(command=lambda: entrada.delete(0, tk.END))
boton_limpiar.grid(row=4, column=0, padx=5, pady=5)

# Ajustar el tamaño de la ventana para que se acomoden los botones
ventana.update()
width = max(ventana.winfo_width(), 300)
height = max(ventana.winfo_height(), 400)
ventana.geometry(f"{width}x{height}")

# Ejecutar el bucle principal
ventana.mainloop()
