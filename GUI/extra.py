import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbmanager import dbManager

def crear_contenido(tab):
    db=dbManager()
    botonRespaldar = ttk.Button(tab, text="RespaldarBD", command=lambda: db.respaldarBD())
    botonRespaldar.place(x=200, y=40)