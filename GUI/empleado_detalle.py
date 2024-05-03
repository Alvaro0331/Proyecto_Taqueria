import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbempleado import *

def empleado_detalles(tree):
    
    def abrir_pestana(event):
        # Obtener el item seleccionado en el Treeview
        item = tree.focus()
        # Obtener los valores del item seleccionado
        valores = tree.item(item, 'values')
        if valores:
            id_empleado = valores[0]  # Primer valor es el ID del empleado
            print("ID del empleado seleccionado:", id_empleado)  # Imprimir el ID en la consola
            # Crear una nueva ventana
            ventana_detalle = tk.Toplevel()
            ventana_detalle.title("Editar Empleado")
            
            # Crear etiquetas y campos de entrada para mostrar los detalles del empleado
            tk.Label(ventana_detalle, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            nombre_entry = tk.Entry(ventana_detalle, width=30)
            nombre_entry.grid(row=0, column=1, padx=5, pady=5)
            
            tk.Label(ventana_detalle, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            telefono_entry = tk.Entry(ventana_detalle, width=30)
            telefono_entry.grid(row=1, column=1, padx=5, pady=5)
            
            tk.Label(ventana_detalle, text="Turno:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
            turno_combobox = ttk.Combobox(ventana_detalle, values=["Matutino", "Vespertino"], state="readonly")
            turno_combobox.grid(row=2, column=1, padx=5, pady=5)
            
            # Agregar botones
            btn_guardar = ttk.Button(ventana_detalle, text="Guardar", command=lambda: actualizar_mesero(id_empleado, nombre_entry.get(), telefono_entry.get(), turno_combobox.get()))
            btn_guardar.grid(row=3, column=0, padx=5, pady=5)

            btn_cancelar = ttk.Button(ventana_detalle, text="Cancelar", command=ventana_detalle.destroy)
            btn_cancelar.grid(row=3, column=1, padx=5, pady=5)
            
            # Llenar los campos de entrada con los valores del registro seleccionado
            nombre_entry.insert(tk.END, valores[1])
            telefono_entry.insert(tk.END, valores[2])
            # Obtener el turno actual del empleado de la columna 4 (índice 3)
            turno_actual = valores[3]
            turno_combobox.set(turno_actual)
        else:
            messagebox.showerror("Error", "Por favor seleccione un empleado.")
            
    return abrir_pestana