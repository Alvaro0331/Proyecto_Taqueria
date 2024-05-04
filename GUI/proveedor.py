import tkinter as tk
from tkinter import END, messagebox, ttk

def crear_contenido(tab):
    #widgets
    nombreLabel=tk.Label(tab, text="Nombre:")
    nombreEntry=tk.Entry(tab,width=50)
    telefonoLabel=tk.Label(tab, text="Teléfono:")
    telefonoEntry=tk.Entry(tab,width=11)
    
    #Boton para registrar nuevo empleado
    botonProvAlta=ttk.Button(tab,text="Registrar proveedor")#, command=lambda: validar_campos(nombreEntry, telefonoEntry, turnoCombobox))
    #boton para ver los empleados registrados
    botonProvList=ttk.Button(tab, text="Lista de proveedores")#, command=empleados_lista)
    
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
    