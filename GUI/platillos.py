import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbplatillo import *
from GUI.platillo_detalle import *

def crear_contenido(tab):
    def actualizar_treeview(tree):
        # Limpiar el contenido actual del Treeview
        tree.delete(*tree.get_children())
        
        # Obtener los resultados de la consulta SQL
        resultados = obtener_platillos()

        # Agregar los resultados actualizados al treeview
        for resultado in resultados:
            tree.insert("", tk.END, values=resultado)

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
    tree["columns"]=("ID","Nombre","Comentarios")
    tree.column("#0", width=0,stretch=tk.NO) #ocultar primera columna
    
    #configurar encabezados
    tree.heading("ID",text="ID")
    tree.heading("Nombre",text="Nombre")
    tree.heading("Comentarios",text="Comentarios")
    # Configurar el ancho del encabezado de la columna "ID" (por ejemplo)
    tree.column("ID", width=1)
    tree.column("Nombre", width=3)
    
    #Obtener los resultados de la consulta SQL
    resultados = obtener_platillos()

    # Agregar los resultados al treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)
    
    # Asignar evento de clic a cada item del Treeview
    tree.bind("<ButtonRelease-1>", platillo_detalle(tree))
    
    # Crear un Frame para contener botones
    frame = tk.Frame(tab)
    frame.pack(fill=tk.BOTH, expand=True)
    #Boton para registrar nuevo platillo
    botonPlatoAlta=ttk.Button(tab,text="Registrar platillo", command= platillo_alta)
    botonPlatoAlta.place(x=100,y=420)
    # Boton para actualizar el contenido del Treeview
    botonActualizar = ttk.Button(tab, text="Actualizar", command=lambda: actualizar_treeview(tree))
    botonActualizar.place(x=100,y=460)
    
def platillo_alta():
    # Crear una nueva ventana
    ventana_alta = tk.Toplevel()
    ventana_alta.title("Alta Platillo")
    
    # Crear etiquetas y campos de entrada para mostrar los detalles del empleado
    tk.Label(ventana_alta, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    nombre_entry = tk.Entry(ventana_alta, width=30)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(ventana_alta, text="Comentarios:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    comentario_entry = tk.Entry(ventana_alta, width=100)
    comentario_entry.grid(row=1, column=1, padx=5, pady=5)
            
    # Agregar botones
    btn_guardar = ttk.Button(ventana_alta, text="Guardar", command=lambda: validar_campos(nombre_entry, comentario_entry))
    btn_guardar.grid(row=3, column=1, padx=5, pady=5)

    btn_cancelar = ttk.Button(ventana_alta, text="Cancelar", command=ventana_alta.destroy)
    btn_cancelar.grid(row=3, column=2, padx=5, pady=5)
    
    # Hacer que la ventana emergente sea modal (bloquee el foco del resto de la aplicación)
    ventana_alta.grab_set()
    ventana_alta.focus_set()
    ventana_alta.wait_window()
    
#Validar que los campos no esten vacios
def validar_campos(nombreEntry, comentarioEntry):
    # Obtener el contenido de los Entry y del Combobox
    nombre = nombreEntry.get()
    comentario = comentarioEntry.get()
    if nombre=='' or comentario=='':
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        alta_platillo(nombre,comentario)