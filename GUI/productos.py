import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbproductos import *
from GUI.producto_detalle import *

def crear_contenido(tab):
    def actualizar_contenido():
        # Limpiar el Treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Obtener resultados de la consulta sql
        resultados = obtener_productos()
        
        # Agregar los resultados al Treeview
        for resultado in resultados:
            tree.insert("", tk.END, values=resultado)
        print("Contenido actualizado")

    # Crear un Frame para contener el Treeview y el Scrollbar
    frame = tk.Frame(tab)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Crear el Treeview
    tree = ttk.Treeview(frame)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Crear un Scrollbar vertical
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Configurar el Treeview para que use el Scrollbar vertical
    tree.configure(yscrollcommand=scrollbar.set)
    
    #configurar columnas
    tree["columns"]=("ID","Nombre","Precio de compra","Existencia")
    tree.column("#0", width=0,stretch=tk.NO) #ocultar primera columna
    
    #configurar encabezados
    tree.heading("ID",text="ID")
    tree.heading("Nombre",text="Nombre")
    tree.heading("Precio de compra",text="Precio de compra")
    tree.heading("Existencia",text="Existencia")
    # Configurar el ancho del encabezado de la columna "ID" (por ejemplo)
    tree.column("ID", width=4)
    tree.column("Nombre", width=20)
    tree.column("Precio de compra", width=3)
    tree.column("Existencia", width=5)
    
    #Obtener los resultados de la consulta SQL
    resultados = obtener_productos()

    # Agregar los resultados al treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)
    
    # Asignar evento de clic a cada item del Treeview
    tree.bind("<ButtonRelease-1>", producto_detalle(tree))
    
    # Crear un Frame para contener botones
    frame = tk.Frame(tab)
    frame.pack(fill=tk.BOTH, expand=True)
    #Boton para registrar nuevo platillo
    botonPlatoAlta=ttk.Button(tab,text="Registrar producto", command= producto_alta)
    botonPlatoAlta.place(x=100,y=420)
    # Boton para actualizar el contenido
    # Boton para actualizar el contenido
    boton_actualizar = ttk.Button(frame, text="Actualizar contenido", command=actualizar_contenido)
    boton_actualizar.pack()

def producto_alta():
    # Crear una nueva ventana
    ventana_alta = tk.Toplevel()
    ventana_alta.title("Alta Producto")
    
    # Crear etiquetas y campos de entrada para mostrar los detalles del empleado
    tk.Label(ventana_alta, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    nombre_entry = tk.Entry(ventana_alta, width=30)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(ventana_alta, text="Precio de compra:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    precio_entry = tk.Entry(ventana_alta, width=7)
    precio_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Agregar botones
    btn_guardar = ttk.Button(ventana_alta, text="Guardar", command=lambda: validar_campos(nombre_entry, precio_entry))
    btn_guardar.grid(row=3, column=1, padx=5, pady=5)

    btn_cancelar = ttk.Button(ventana_alta, text="Cancelar", command=ventana_alta.destroy)
    btn_cancelar.grid(row=3, column=2, padx=5, pady=5)
    
#Validar que los campos no esten vacios
def validar_campos(nombreEntry, precioEntry):
    # Obtener el contenido de los Entry y del Combobox
    nombre = nombreEntry.get()
    precio = precioEntry.get()
    if nombre=='' or precio=='':
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        alta_productos(nombre,precio)