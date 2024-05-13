import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbcomandas import *
from GUI.comanda_detalle import *

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
    tree["columns"]=("Folio","Fecha","Mesa","Total a pagar")
    tree.column("#0", width=0,stretch=tk.NO) #ocultar primera columna
    
    #configurar encabezados
    tree.heading("Folio",text="Folio")
    tree.heading("Fecha",text="Fecha")
    tree.heading("Mesa",text="Mesa")
    tree.heading("Total a pagar",text="Total a pagar")
    
    #Obtener los resultados de la consulta SQL
    resultados = obtener_comandas()

    # Agregar los resultados al treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)
    
    # Asignar evento de clic a cada item del Treeview
    tree.bind("<ButtonRelease-1>", detalle_comanda(tree))