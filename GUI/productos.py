import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbplatillo import *

def crear_contenido(tab):
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
    tree.column("ID", width=1)
    tree.column("Nombre", width=3)
    
    # Crear un Frame para contener botones
    frame = tk.Frame(tab)
    frame.pack(fill=tk.BOTH, expand=True)
    #Boton para registrar nuevo platillo
    botonPlatoAlta=ttk.Button(tab,text="Registrar producto")#, command= platillo_alta)
    botonPlatoAlta.place(x=100,y=420)