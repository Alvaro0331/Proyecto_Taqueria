import tkinter as tk
from tkinter import END, messagebox, ttk
from GUI.empleados import crear_contenido as empleados
from GUI.proveedor import crear_contenido as proveedores
from GUI.platillos import crear_contenido as platillos
from GUI.productos import crear_contenido as productos
from GUI.comandas import crear_contenido as comandas
from GUI.mesas import crear_contenido as mesas
from GUI.facturas import crear_contenido as factura

def run_app():
    root=tk.Tk()
    root.title("Taquería Don Alvaro")
    root.geometry("1050x600")
    
    notebook=ttk.Notebook(root)
    
    #Pestañas del notebook
    tab1=ttk.Frame(notebook)
    tab2=ttk.Frame(notebook)
    tab3=ttk.Frame(notebook)
    tab4=ttk.Frame(notebook)
    tab5=ttk.Frame(notebook)
    tab6=ttk.Frame(notebook)
    tab7=ttk.Frame(notebook)
    
    #Agregar contenido a las pestañas del notebook
    mesas(tab1)
    empleados(tab2)
    proveedores(tab3)
    platillos(tab4)
    productos(tab5)
    comandas(tab6)
    factura(tab7)
    
    #agregar pestañas al notebook
    notebook.add(tab1, text="Mesas")
    notebook.add(tab2, text="Meseros")
    notebook.add(tab3, text="Proveedores")
    notebook.add(tab4, text="Platillos")
    notebook.add(tab5, text="Productos")
    notebook.add(tab6, text="Comandas")
    notebook.add(tab7, text="Facturas")
    
    #Colocar notebook en la pestaña principal
    notebook.pack(expand=True, fill="both")
    
    root.mainloop()