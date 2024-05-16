import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbproductos import *

def producto_detalle(tree):
    
    def abrir_pestana(event):
        # Obtener el item seleccionado en el Treeview
        item = tree.focus()
        # Obtener los valores del item seleccionado
        valores = tree.item(item, 'values')
        if valores:
            id_producto = valores[0]  # Primer valor es el ID del empleado
            print("ID del producto seleccionado:", id_producto)  # Imprimir el ID en la consola
            # Crear una nueva ventana
            ventana_detalle = tk.Toplevel()
            ventana_detalle.title("Editar Producto")
            
            # Crear etiquetas y campos de entrada para mostrar los detalles del producto
            tk.Label(ventana_detalle, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            nombre_entry = tk.Entry(ventana_detalle, width=30)
            nombre_entry.grid(row=0, column=1, padx=5, pady=5)
            
            tk.Label(ventana_detalle, text="Precio de compra:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            precio_entry = tk.Entry(ventana_detalle, width=7)
            precio_entry.grid(row=1, column=1, padx=5, pady=5)
            
            tk.Label(ventana_detalle, text="Existencia:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
            existencia_entry = tk.Entry(ventana_detalle, width=7)
            existencia_entry.grid(row=2, column=1, padx=5, pady=5)
            
            # Agregar botones
            btn_guardar = ttk.Button(ventana_detalle, text="Guardar", command=lambda: actualizar_producto(id_producto, nombre_entry.get(), precio_entry.get(),existencia_entry.get()))
            btn_guardar.grid(row=3, column=0, padx=5, pady=5)

            btn_cancelar = ttk.Button(ventana_detalle, text="Cancelar", command=ventana_detalle.destroy)
            btn_cancelar.grid(row=3, column=1, padx=5, pady=5)
            
            # Llenar los campos de entrada con los valores del registro seleccionado
            nombre_entry.insert(tk.END, valores[1])
            precio_entry.insert(tk.END, valores[2])
            existencia_entry.insert(tk.END, valores[3])
            
            # Hacer que la ventana emergente sea modal (bloquee el foco del resto de la aplicación)
            ventana_detalle.grab_set()
            ventana_detalle.focus_set()
            ventana_detalle.wait_window()
        else:
            messagebox.showerror("Error", "Por favor seleccione un producto.")
            
    return abrir_pestana