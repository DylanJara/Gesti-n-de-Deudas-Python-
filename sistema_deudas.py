import tkinter as tk
from tkinter import messagebox, simpledialog

clientes = {}

def agregar_cliente():
    nombre = simpledialog.askstring("Agregar cliente", "Nombre del cliente:")
    if nombre:
        if nombre not in clientes:
            clientes[nombre] = []
            messagebox.showinfo("Éxito", f"Cliente '{nombre}' agregado.")
        else:
            messagebox.showwarning("Atención", "El cliente ya existe.")

def agregar_deuda():
    nombre = simpledialog.askstring("Agregar deuda", "Nombre del cliente:")
    if nombre in clientes:
        producto = simpledialog.askstring("Producto", "¿Qué llevó?")
        monto = simpledialog.askfloat("Monto", "¿Cuánto debe?")
        if producto and monto:
            clientes[nombre].append((producto, monto))
            messagebox.showinfo("Agregado", f"Deuda registrada: {producto} - Gs. {monto}")
    else:
        messagebox.showerror("Error", "El cliente no existe.")

def ver_deudas():
    nombre = simpledialog.askstring("Ver deudas", "Nombre del cliente:")
    if nombre in clientes:
        deudas = clientes[nombre]
        if not deudas:
            mensaje = "No tiene deudas."
        else:
            mensaje = "\n".join([f"{producto} - Gs. {monto}" for producto, monto in deudas])
            total = sum(monto for _, monto in deudas)
            mensaje += f"\n\nTotal: Gs. {total}"
        messagebox.showinfo(f"Deudas de {nombre}", mensaje)
    else:
        messagebox.showerror("Error", "El cliente no existe.")

def marcar_pagado():
    nombre = simpledialog.askstring("Pagar deuda", "Nombre del cliente:")
    if nombre in clientes:
        clientes[nombre].clear()
        messagebox.showinfo("Pagado", f"Todas las deudas de '{nombre}' han sido marcadas como pagadas.")
    else:
        messagebox.showerror("Error", "El cliente no existe.")

# Interfaz
ventana = tk.Tk()
ventana.title("Sistema de Deudas")
ventana.geometry("300x300")

tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente).pack(pady=5)
tk.Button(ventana, text="Agregar Deuda", command=agregar_deuda).pack(pady=5)
tk.Button(ventana, text="Ver Deudas", command=ver_deudas).pack(pady=5)
tk.Button(ventana, text="Marcar como Pagado", command=marcar_pagado).pack(pady=5)

ventana.mainloop()
