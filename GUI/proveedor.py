import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbproveedor import *
from GUI.proveedor_detalle import *

def crear_contenido(tab):
    #widgets
    nombreLabel=tk.Label(tab, text="Proveedor:")
    nombreEntry=tk.Entry(tab,width=50)
    telefonoLabel=tk.Label(tab, text="Teléfono:")
    telefonoEntry=tk.Entry(tab,width=11)
    
    #Boton para registrar nuevo empleado
    botonProvAlta=ttk.Button(tab,text="Registrar proveedor", command=lambda: validar_campos(nombreEntry, telefonoEntry))
    #boton para ver los empleados registrados
    botonProvList=ttk.Button(tab, text="Lista de proveedores", command=proveedor_lista)
    
    #Colocar widgets
    nombreLabel.place(x=20, y=20)
    nombreEntry.place(x=100, y=20)
    telefonoLabel.place(x=20, y=50)
    telefonoEntry.place(x=100, y=50)
    botonProvAlta.place(x=100,y=120)
    botonProvList.place(x=250, y=120)
    
#Validar que los campos no esten vacios
def validar_campos(nombreEntry, telefonoEntry):
    # Obtener el contenido de los Entry y del Combobox
    nombre = nombreEntry.get()
    telefono = telefonoEntry.get()
    if nombre=='' or telefono=='':
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        proveedor_alta(nombre,telefono)

def proveedor_lista():
    #mostrar una nueva ventana
    ventana_empleados=tk.Toplevel()
    ventana_empleados.title("Lista de proveedores")
    
    # Crear un Frame para contener el Treeview y el Scrollbar
    frame = tk.Frame(ventana_empleados)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Crear el Treeview
    tree = ttk.Treeview(frame)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Crear un Scrollbar vertical
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Configurar el Treeview para que use el Scrollbar vertical
    tree.configure(yscrollcommand=scrollbar.set)
    
    # Configurar columnas
    tree["columns"] = ("ID", "Nombre", "Telefono")
    tree.column("#0", width=0, stretch=tk.NO)  # Ocultar primera columna
    
    # Configurar encabezados
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Telefono", text="Telefono")
    
    # Obtener los resultados de la consulta SQL
    resultados = obtener_proveedores()

    # Agregar los resultados al treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)
        
    # Asignar evento de clic a cada item del Treeview
    tree.bind("<ButtonRelease-1>", proveedor_detalles(tree))