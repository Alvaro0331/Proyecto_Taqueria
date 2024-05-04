import tkinter as tk
from tkinter import END, messagebox, ttk
from GUI.empleado_detalle import *

def crear_contenido(tab):
    #widgets
    nombreLabel=tk.Label(tab, text="Nombre:")
    nombreEntry=tk.Entry(tab,width=50)
    telefonoLabel=tk.Label(tab, text="Teléfono:")
    telefonoEntry=tk.Entry(tab,width=11)
    # Lista de opciones para el Combobox
    opciones = ["Matutino", "Vespertino"]
    turnoLabel=tk.Label(tab, text="Turno:")
    turnoCombobox=ttk.Combobox(tab,values=opciones,state="readonly")
    #Boton para registrar nuevo empleado
    botonEmpleadoAlta=ttk.Button(tab,text="Registrar empleado", command=lambda: validar_campos(nombreEntry, telefonoEntry, turnoCombobox))
    #boton para ver los empleados registrados
    botonEmpleadosList=ttk.Button(tab, text="Lista de empleados", command=empleados_lista)
    
    #Colocar widgets
    nombreLabel.place(x=20, y=20)
    nombreEntry.place(x=100, y=20)
    telefonoLabel.place(x=20, y=50)
    telefonoEntry.place(x=100, y=50)
    turnoLabel.place(x=20, y=80)
    turnoCombobox.place(x=100, y=80)
    botonEmpleadoAlta.place(x=100,y=120)
    botonEmpleadosList.place(x=250, y=120)
    
#Validar que los campos no esten vacios
def validar_campos(nombreEntry, telefonoEntry, turnoCombobox):
    # Obtener el contenido de los Entry y del Combobox
    nombre = nombreEntry.get()
    telefono = telefonoEntry.get()
    turno = turnoCombobox.get()
    if nombre=='' or telefono=='' or turno=='':
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        mesero_alta(nombre,telefono,turno)

def empleados_lista():
    #mostrar una nueva ventana
    ventana_empleados=tk.Toplevel()
    ventana_empleados.title("Lista de empleados")
    
    # Crear un Frame para contener el Treeview y el Scrollbar
    frame = tk.Frame(ventana_empleados)
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
    tree["columns"]=("ID","Nombre","Telefono","Turno")
    tree.column("#0", width=0,stretch=tk.NO) #ocultar primera columna
    
    #configurar encabezados
    tree.heading("ID",text="ID")
    tree.heading("Nombre",text="Nombre")
    tree.heading("Telefono",text="Telefono")
    tree.heading("Turno",text="Turno")
    
    # Obtener los resultados de la consulta SQL utilizando la función obtener_meseros() de DbManager
    resultados = obtener_meseros()

    # Agregar los resultados al treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)
        
    # Asignar evento de clic a cada item del Treeview
    tree.bind("<ButtonRelease-1>", empleado_detalles(tree))
