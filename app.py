import tkinter as tk
from tkinter import END, messagebox, ttk
from GUI.empleados import crear_contenido as empleados

def run_app():
    root=tk.Tk()
    root.title("Taquería Don Alvaro")
    root.geometry("800x600")
    
    notebook=ttk.Notebook(root)
    
    #Pestañas del notebook
    tab1=ttk.Frame(notebook)
    
    
    #Agregar contenido a las pestañas del notebook
    empleados(tab1)
    
    #agregar pestañas al notebook
    notebook.add(tab1, text="Empleados")
    
    
    #Colocar notebook en la pestaña principal
    notebook.pack(expand=True, fill="both")
    
    root.mainloop()