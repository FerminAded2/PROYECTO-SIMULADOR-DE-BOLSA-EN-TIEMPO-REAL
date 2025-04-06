import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Simulador de Bolsa en Tiempo Real")

label_cronometro = tk.Label(ventana, text="Tiempo Restante: 10:00", font=("Arial", 16))
label_cronometro.grid(row=0, column=1)

label_dinero_restante = tk.Label(ventana, text="Dinero Restante: $1000", font=("Arial", 12))
label_dinero_restante.grid(row=1, column=0, sticky="w")

label_dinero_invertido = tk.Label(ventana, text="Dinero Invertido: $0", font=("Arial", 12))
label_dinero_invertido.grid(row=2, column=0, sticky="w")

treeview = ttk.Treeview(ventana, columns=("Acción", "Precio"))
treeview.heading("#1", text="Acción")
treeview.heading("#2", text="Precio")
treeview.grid(row=1, column=1, rowspan=4, padx=10)

entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=1, column=2)

button_comprar = tk.Button(ventana, text="Comprar")
button_comprar.grid(row=1, column=3)

button_vender = tk.Button(ventana, text="Vender")
button_vender.grid(row=1, column=4)


ventana.mainloop()


