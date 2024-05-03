import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbempleado import *
from GUI.empleado_detalle import *

def crear_contenido(tab):
    #widgets
    nombreLabel=tk.Label(tab, text="Nombre:")
    nombreEntry=tk.Entry(tab,width=50)
    telefonoLabel=tk.Label(tab, text="Teléfono:")
    telefonoEntry=tk.Entry(tab,width=11)
    # Lista de opciones para el Combobox
    opciones = ["Matutino", "Vespertino"]
    turnoLabel=tk.Label(tab, text="Turno:")
    turnoCombobox=ttk.Combobox(tab,values=opciones,state="readonly")
    
    #boton para ver los empleados registrados
    botonEmpleados=ttk.Button(tab, text="Lista de empleados", command=empleados_lista)
    
    #Colocar widgets
    nombreLabel.grid(row=0, column=0)
    nombreEntry.grid(row=0, column=1)
    telefonoLabel.grid(row=1,column=0)
    telefonoEntry.grid(row=1, column=1)
    botonEmpleados.grid(row=4,column=2)
    turnoLabel.grid(row=3,column=0)
    turnoCombobox.grid(row=3, column=1)
    
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
    
    # Obtener los resultados de la consulta SQL utilizando la función obtener_meseros() de DbManager
    resultados = obtener_meseros()

    # Agregar los resultados al treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)
        
    # Asignar evento de clic a cada item del Treeview
    tree.bind("<ButtonRelease-1>", empleado_detalles(tree))
