import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbplatillo import *

def platillo_detalle(tree):
    
    def abrir_pestana(event):
        # Obtener el item seleccionado en el Treeview
        item = tree.focus()
        # Obtener los valores del item seleccionado
        valores = tree.item(item, 'values')
        if valores:
            id_platillo = valores[0]  # Primer valor es el ID del empleado
            print("ID del platillo seleccionado:", id_platillo)  # Imprimir el ID en la consola
            # Crear una nueva ventana
            ventana_detalle = tk.Toplevel()
            ventana_detalle.title("Editar Platillo")
            
            # Crear etiquetas y campos de entrada para mostrar los detalles del empleado
            tk.Label(ventana_detalle, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            nombre_entry = tk.Entry(ventana_detalle, width=30)
            nombre_entry.grid(row=0, column=1, padx=5, pady=5)
            
            tk.Label(ventana_detalle, text="Comentarios:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            comentario_entry = tk.Entry(ventana_detalle, width=100)
            comentario_entry.grid(row=1, column=1, padx=5, pady=5)
            
            # Agregar botones
            btn_guardar = ttk.Button(ventana_detalle, text="Guardar", command=lambda: actualizar_platillo(id_platillo, nombre_entry.get(), comentario_entry.get()))
            btn_guardar.grid(row=3, column=0, padx=5, pady=5)

            btn_cancelar = ttk.Button(ventana_detalle, text="Cancelar", command=ventana_detalle.destroy)
            btn_cancelar.grid(row=3, column=1, padx=5, pady=5)
            
            # Llenar los campos de entrada con los valores del registro seleccionado
            nombre_entry.insert(tk.END, valores[1])
            comentario_entry.insert(tk.END, valores[2])
        else:
            messagebox.showerror("Error", "Por favor seleccione un empleado.")
            
    return abrir_pestana