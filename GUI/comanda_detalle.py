import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbcomandas import *

def detalle_comanda(tree):
    def abrir_pestana(event):
        # Obtener el item seleccionado en el Treeview
        item = tree.focus()
        # Obtener los valores del item seleccionado
        valores = tree.item(item, 'values')
        if valores:
            id_platillo = valores[0]  # Primer valor es el ID del empleado
            print("ID de la comanda seleccionada:", id_platillo)  # Imprimir el ID en la consola
            # Crear una nueva ventana
            ventana_detalle = tk.Toplevel()
            ventana_detalle.title("Detalle Comanda")
            
            # Agregar encabezados
            encabezados = ["Folio", "Fecha", "Mesa", "Total a pagar"]
            for i, encabezado in enumerate(encabezados):
                label_encabezado = tk.Label(ventana_detalle, text=encabezado)
                label_encabezado.grid(row=0, column=i)
            
            # Mostrar los valores obtenidos
            for i, valor in enumerate(valores):
                label_valor = tk.Label(ventana_detalle, text=valor)
                label_valor.grid(row=1, column=i)
            
            # Agregar un Treeview
            tree_detalle = ttk.Treeview(ventana_detalle, columns=("Columna1", "Columna2", "Columna3"))
            tree_detalle.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

            # Configurar encabezados del Treeview
            tree_detalle.heading("#0", text="ID")
            tree_detalle.heading("Columna1", text="Nombre")
            tree_detalle.heading("Columna2", text="Cantidad")
            tree_detalle.heading("Columna3", text="Precio")
    return abrir_pestana