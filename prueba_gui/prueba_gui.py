# prueba_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import Api_con_alpha as api
import random
import time
import threading
import os
import datetime

# ---------------- PARAMETROS ---------------- #
SIMBOLO = "AAPL"
API_KEY = "0L7EQWQLYVQNJWJR"
TIEMPO_LIMITE = 600
SALDO_INICIAL = 10000

# ---------------- VARIABLES ---------------- #
saldo = SALDO_INICIAL
empresas = ["Samsung", "IBM", "Mercado Libre", "Amazon"]
precios = {}
precios_anteriores = {}
portafolio = {emp: {"acciones": 0.0, "invertido": 0.0} for emp in empresas}
modo_operacion = "compra"
inicio_tiempo = None
simulacion_activa = False

# ---------------- FUNCIONES ---------------- #
def actualizar_interfaz():
    label_dinero.config(text=f"Dinero: ${saldo:.2f}")
    for i in tabla_acciones.get_children():
        tabla_acciones.delete(i)
    for emp in empresas:
        precio = precios[emp]
        precio_ant = precios_anteriores.get(emp, precio)
        color = "green" if precio > precio_ant else "red" if precio < precio_ant else "black"
        tabla_acciones.insert("", "end", values=(emp, f"{precio:.2f}"))

    for i in tabla_portafolio.get_children():
        tabla_portafolio.delete(i)
    for emp in empresas:
        acc = portafolio[emp]["acciones"]
        inv = portafolio[emp]["invertido"]
        if acc > 0:
            valor_actual = acc * precios[emp]
            ganancia = valor_actual - inv
            tabla_portafolio.insert("", "end", values=(emp, f"{acc:.2f}", f"${inv:.2f}", f"${ganancia:.2f}"))

def operar():
    global saldo
    emp = combo_empresa.get()
    try:
        monto = int(entry_cantidad.get())
    except ValueError:
        messagebox.showwarning("Cantidad inválida", "Ingresá un número válido.")
        return

    if emp not in empresas:
        messagebox.showwarning("Empresa no seleccionada", "Seleccioná una empresa.")
        return

    precio_unitario = precios[emp]

    if modo_operacion == "compra":
        if saldo >= monto:
            acciones_compradas = monto / precio_unitario
            saldo -= monto
            portafolio[emp]["acciones"] += acciones_compradas
            portafolio[emp]["invertido"] += monto
        else:
            messagebox.showwarning("Sin saldo", "No tenés suficiente dinero.")

    elif modo_operacion == "venta":
        acciones_disponibles = portafolio[emp]["acciones"]
        acciones_a_vender = monto / precio_unitario
        if acciones_disponibles >= acciones_a_vender:
            saldo += monto
            portafolio[emp]["acciones"] -= acciones_a_vender
            portafolio[emp]["invertido"] -= acciones_a_vender * precio_unitario
        else:
            messagebox.showwarning("Sin fondos", "No tenés suficientes acciones.")

    actualizar_interfaz()

def setear_modo(m):
    global modo_operacion
    modo_operacion = m

def iniciar_cronometro():
    global inicio_tiempo, simulacion_activa
    inicio_tiempo = time.time()
    simulacion_activa = True

    def cuenta():
        while True:
            t = time.time() - inicio_tiempo
            restante = TIEMPO_LIMITE - int(t)
            if restante <= 0:
                label_tiempo.config(text="Tiempo: 00:00")
                resumen_final()
                break
            minutos = restante // 60
            segundos = restante % 60
            label_tiempo.config(text=f"Tiempo: {int(minutos):02}:{int(segundos):02}")
            time.sleep(1)

    def fluctuar_precios():
        while simulacion_activa:
            for emp in empresas:
                precios_anteriores[emp] = precios[emp]
                cambio = random.uniform(-0.03, 0.03)
                precios[emp] = round(precios[emp] * (1 + cambio), 2)
            actualizar_interfaz()
            time.sleep(2)

    threading.Thread(target=cuenta, daemon=True).start()
    threading.Thread(target=fluctuar_precios, daemon=True).start()

def resumen_final():
    global simulacion_activa
    simulacion_activa = False
    mensaje = f"--- RESUMEN FINAL ---\nSaldo: ${saldo:.2f}\n\nPORTAFOLIO:\n"
    for emp, data in portafolio.items():
        if data["acciones"] > 0:
            mensaje += f"{emp}: {data['acciones']:.2f} acciones, Invertido: ${data['invertido']:.2f}\n"
    messagebox.showinfo("Resumen", mensaje)
    ventana.destroy()

def agregar_monto(monto):
    actual = entry_cantidad.get()
    try:
        actual_val = int(actual) if actual else 0
    except ValueError:
        actual_val = 0
    entry_cantidad.delete(0, tk.END)
    entry_cantidad.insert(0, str(actual_val + monto))

# ---------------- GUI ---------------- #
ventana = tk.Tk()
ventana.title("Simulador de Bolsa")
ventana.geometry("1200x500")

# Imagen decorativa a la derecha
ruta_img = os.path.join(os.path.dirname(__file__), "fondo_de_la_ciudad.png")
imagen_raw = Image.open(ruta_img).resize((300, 400))
imagen_tk = ImageTk.PhotoImage(imagen_raw)
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack(side="right", padx=10, pady=10)

# Top bar
frame_top = tk.Frame(ventana)
frame_top.pack(fill="x")
label_tiempo = tk.Label(frame_top, text="Tiempo: 10:00", font=("Arial", 12))
label_tiempo.pack(side="left", padx=10, pady=5)
label_dinero = tk.Label(frame_top, text=f"Dinero: ${saldo:.2f}", font=("Arial", 12))
label_dinero.pack(side="right", padx=10, pady=5)

# Tablas
frame_tablas = tk.Frame(ventana)
frame_tablas.pack(expand=True, fill="both")

tabla_acciones = ttk.Treeview(frame_tablas, columns=("Accion", "Precio"), show="headings", height=10)
tabla_acciones.heading("Accion", text="Acción")
tabla_acciones.heading("Precio", text="Precio ($)")
tabla_acciones.column("Accion", width=150)
tabla_acciones.column("Precio", width=100)
tabla_acciones.pack(side="left", expand=True, fill="y", padx=10)

tabla_portafolio = ttk.Treeview(frame_tablas, columns=("Accion", "Cantidad", "Invertido", "Ganancia"), show="headings", height=10)
tabla_portafolio.heading("Accion", text="Acción")
tabla_portafolio.heading("Cantidad", text="Acciones")
tabla_portafolio.heading("Invertido", text="Invertido")
tabla_portafolio.heading("Ganancia", text="Ganancia/Pérdida")
tabla_portafolio.column("Accion", width=120)
tabla_portafolio.column("Cantidad", width=100)
tabla_portafolio.column("Invertido", width=100)
tabla_portafolio.column("Ganancia", width=120)
tabla_portafolio.pack(side="left", expand=True, fill="y", padx=10)

frame_controls = tk.Frame(ventana)
frame_controls.pack(fill="x", pady=10)

combo_empresa = ttk.Combobox(frame_controls, values=empresas, width=15)
combo_empresa.set("Acción:")
combo_empresa.pack(side="left", padx=5)

entry_cantidad = tk.Entry(frame_controls, width=10)
entry_cantidad.pack(side="left")

for monto in [500, 1000, 2000]:
    tk.Button(frame_controls, text=str(monto), width=5, command=lambda m=monto: agregar_monto(m)).pack(side="left", padx=2)

tk.Button(frame_controls, text="Comprar", command=lambda: [setear_modo("compra"), operar()]).pack(side="left", padx=5)
tk.Button(frame_controls, text="Vender", command=lambda: [setear_modo("venta"), operar()]).pack(side="left", padx=5)
tk.Button(frame_controls, text="Iniciar", command=iniciar_cronometro).pack(side="right", padx=10)

# ---------------- OBTENCIÓN DE DATOS ---------------- #
datos = api.obtener_datos(API_KEY, SIMBOLO)
ultima_fecha = list(datos["Time Series (Daily)"].keys())[0]
precio_base = float(datos["Time Series (Daily)"][ultima_fecha]["4. close"])

for emp in empresas:
    precios[emp] = round(precio_base * random.uniform(0.8, 1.2), 2)
    precios_anteriores[emp] = precios[emp]

actualizar_interfaz()
ventana.mainloop()

