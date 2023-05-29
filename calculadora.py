import tkinter as tk

# Función para evaluar la expresión matemática
def evaluar():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Función para agregar números y operadores al campo de entrada
def agregar_caracter(caracter):
    entry.insert(tk.END, caracter)

# Función para borrar el último carácter del campo de entrada
def borrar_caracter():
    entry.delete(len(entry.get()) - 1, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear el campo de entrada
entry = tk.Entry(ventana, font=("Arial", 14), justify=tk.RIGHT, width=15)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones numéricos
for i in range(9):
    boton = tk.Button(ventana, text=str(i+1), font=("Arial", 12), width=5,
                      command=lambda i=i: agregar_caracter(str(i+1)))
    boton.grid(row=1 + (i // 3), column=i % 3, padx=5, pady=5)

# Crear los botones de los operadores
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    boton = tk.Button(ventana, text=operador, font=("Arial", 12), width=5,
                      command=lambda operador=operador: agregar_caracter(operador))
    boton.grid(row=i+2, column=3, padx=5, pady=5)

# Crear el botón de igual
boton_igual = tk.Button(ventana, text="=", font=("Arial", 12), width=5, command=evaluar)
boton_igual.grid(row=5, column=2, padx=5, pady=5)

# Crear el botón de borrar
boton_borrar = tk.Button(ventana, text="C", font=("Arial", 12), width=5, command=borrar_caracter)
boton_borrar.grid(row=5, column=0, padx=5, pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
