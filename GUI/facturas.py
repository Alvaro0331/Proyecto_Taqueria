import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbfacturas import *

def crear_contenido(tab):
    # Crear un Frame para contener el Treeview y el Scrollbar
    frame = tk.Frame(tab)
    frame.pack(fill=tk.BOTH, expand=True)
    # Crear el Treeview para mostrar las comandas
    treeview = ttk.Treeview(frame, columns=("Folio de factura", "Fecha", "FK_Proveedor", "Proveedor"), show="headings")
    treeview.heading("Folio de factura", text="Folio de factura")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("FK_Proveedor", text="ID Proveedor")
    treeview.heading("Proveedor", text="Proveedor")
    
    # Crear el scrollbar vertical
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=treeview.yview)
    scrollbar.pack(side="right", fill="y")

    treeview.configure(yscrollcommand=scrollbar.set)
    
    treeview.pack(fill=tk.BOTH, expand=True)
    
    #Obtener resultados de la consulta sql
    resultados=obtener_facturas()
    
    # Agregar los resultados al treeview
    for resultado in resultados:
        treeview.insert("", tk.END, values=resultado)
    
    #Agregar el evento select al treeview
    treeview.bind("<<TreeviewSelect>>")#, lambda event: detalles_facturas(treeview))
    
    # Crear un Frame para contener formulario
    frame = tk.Frame(tab)
    frame.pack(fill=tk.BOTH, expand=True)