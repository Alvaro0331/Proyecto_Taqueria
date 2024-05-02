import tkinter as tk
from tkinter import END, messagebox, ttk

def crear_contenido(tab):
    label=tk.Label(tab, text="Pestaña empleados").pack(padx=10, pady=10)
    
    #boton para ver los empleados registrados
    boton=ttk.Button(tab, text="Lista de empleados", command=empleados_lista).pack(pady=10)
    
def empleados_lista():
    #mostrar una nueva ventana
    ventana_empleados=tk.Toplevel()
    ventana_empleados.title("Lista de empleados")
    
    #crear treeview
    tree = ttk.Treeview(ventana_empleados)
    tree.pack(expand=True, fill=tk.BOTH)
    #configurar columnas
    tree["columns"]=("ID","Nombre","Telefono","Turno")
    tree.column("#0", width=0,stretch=tk.NO) #ocultar primera columna
    
    #configurar encabezados
    tree.heading("ID",text="ID")
    tree.heading("Nombre",text="Nombre")
    tree.heading("Telefono",text="Telefono")
    tree.heading("Turno",text="Turno")
    
