import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbmesas import * 

def crear_contenido(tab):
    #widgets
    mesaLabel=tk.Label(tab, text="Numero de clientes:")
    mesaEntry=tk.Entry(tab,width=5)
    # Lista de opciones para el Combobox
    opciones = obtener_meseros()
    meseroLabel=tk.Label(tab, text="Mesero:")
    meseroCombobox=ttk.Combobox(tab,values=opciones,state="readonly")
    #Boton para registrar nuevo empleado
    botonMesaAlta=ttk.Button(tab,text="Abrir mesa", command=lambda: validar_campos(mesaEntry,meseroCombobox))
    
    #Colocar widgets
    mesaLabel.place(x=20, y=20)
    mesaEntry.place(x=150, y=20)
    meseroLabel.place(x=20, y=50)
    meseroCombobox.place(x=100, y=50)
    botonMesaAlta.place(x=100,y=120)
    
def validar_campos(mesaEntry,meseroCombobox):
    mesero=meseroCombobox.get()
    clientes=mesaEntry.get()
    
    if not mesero or not clientes:
        messagebox.showerror("Error", "Faltan campos por llenar")
    else:
        alta_mesa(mesero,clientes)