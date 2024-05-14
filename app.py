import tkinter as tk
from tkinter import END, messagebox, ttk
from GUI.empleados import crear_contenido as empleados
from GUI.proveedor import crear_contenido as proveedores
from GUI.platillos import crear_contenido as platillos
from GUI.productos import crear_contenido as productos
from GUI.comandas import crear_contenido as comandas

def run_app():
    root=tk.Tk()
    root.title("Taquería Don Alvaro")
    root.geometry("800x600")
    
    notebook=ttk.Notebook(root)
    
    #Pestañas del notebook
    tab1=ttk.Frame(notebook)
    tab2=ttk.Frame(notebook)
    tab3=ttk.Frame(notebook)
    tab4=ttk.Frame(notebook)
    tab5=ttk.Frame(notebook)
    
    
    #Agregar contenido a las pestañas del notebook
    empleados(tab1)
    proveedores(tab2)
    platillos(tab3)
    productos(tab4)
    comandas(tab5)
    
    #agregar pestañas al notebook
    notebook.add(tab1, text="Empleados")
    notebook.add(tab2, text="Proveedores")
    notebook.add(tab3, text="Platillos")
    notebook.add(tab4, text="Productos")
    notebook.add(tab5, text="Comandas")
    
    #Colocar notebook en la pestaña principal
    notebook.pack(expand=True, fill="both")
    
    root.mainloop()