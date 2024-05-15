import tkinter as tk
from tkinter import END, messagebox, ttk
from DB.dbcomandas import *

def crear_contenido(tab):
    # Crear el Treeview para mostrar las comandas
    treeview = ttk.Treeview(tab, columns=("Numero_Folio", "Fecha", "FK_Mesa", "Total_Pagar"), show="headings")
    treeview.heading("Numero_Folio", text="Número de Folio")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("FK_Mesa", text="Mesa")
    treeview.heading("Total_Pagar", text="Total a Pagar")
    
    # Crear el scrollbar vertical
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=treeview.yview)
    scrollbar.pack(side="right", fill="y")

    treeview.configure(yscrollcommand=scrollbar.set)
    
    treeview.pack(fill=tk.BOTH, expand=True)

    #Obtener resultados de la consulta sql
    resultados=obtener_comandas()
    
    # Agregar los resultados al treeview
    for resultado in resultados:
        treeview.insert("", tk.END, values=resultado)
    
    #Agregar el evento select al treeview
    treeview.bind("<<TreeviewSelect>>", lambda event: detalles_comanda(treeview))


###Ventana detalle comanda###
def detalles_comanda(treeview):
    # Obtener el registro seleccionado
    item = treeview.focus()

    # Obtener los detalles del registro seleccionado
    detalles = treeview.item(item, "values")
    
    if detalles:
        id_comanda = detalles[0]  # Primer valor es el ID del empleado
        print("ID de la comanda seleccionada:", id_comanda)  # Imprimir el ID en la consola
        # Crear y configurar la ventana emergente
        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("Detalles de la comanda")
        
        # Crear frame para el Treeview
        frame_treeview = tk.Frame(ventana_emergente)
        frame_treeview.pack(pady=10, fill="both", expand=True)

        # Crear el Treeview para mostrar los detalles de la comanda
        treeview_detalles = ttk.Treeview(ventana_emergente, columns=("ID_DetalleC", "Cantidad", "Hora", "Precio_Venta", "FK_Producto", "FK_Platillo"), show="headings")
        treeview_detalles.heading("ID_DetalleC", text="ID Detalle")
        treeview_detalles.heading("Cantidad", text="Cantidad")
        treeview_detalles.heading("Hora", text="Hora")
        treeview_detalles.heading("Precio_Venta", text="Precio Venta")
        treeview_detalles.heading("FK_Producto", text="FK Producto")
        treeview_detalles.heading("FK_Platillo", text="FK Platillo")
        
        # Agregar scrollbar vertical
        scrollbar_y = ttk.Scrollbar(ventana_emergente, orient="vertical", command=treeview_detalles.yview)
        scrollbar_y.pack(side="right", fill="y")
        treeview_detalles.configure(yscrollcommand=scrollbar_y.set)
        
        #Obtener los resultados de la consulta SQL
        resultados = obtener_detalle_comanda(id_comanda)

        # Agregar los resultados al treeview
        for resultado in resultados:
            treeview_detalles.insert("", tk.END, values=resultado)

        treeview_detalles.pack(fill=tk.BOTH, expand=True)

        ##Formulario para agregar productos al detalle##
        # Crear frame para el formulario de agregar productos
        frame_formulario = tk.Frame(ventana_emergente)
        frame_formulario.pack(pady=10)
        
        #Obtener platillos y productos disponibles
        productos=productos_disponibles()
        platillos=platillos_disponibles()

        # Campos del formulario
        lbl_producto = tk.Label(frame_formulario, text="Producto:")
        lbl_producto.grid(row=0, column=0, padx=5)
        
        combo_producto = ttk.Combobox(frame_formulario, values=[f"{nombre} ({tipo})" for _, nombre, tipo in productos + platillos])
        combo_producto.grid(row=0, column=1, padx=5)

        entry_producto = tk.Entry(frame_formulario)
        entry_producto.grid(row=0, column=1, padx=5)

        lbl_cantidad = tk.Label(frame_formulario, text="Cantidad:")
        lbl_cantidad.grid(row=1, column=0, padx=5)
        
        

        entry_cantidad = tk.Entry(frame_formulario)
        entry_cantidad.grid(row=1, column=1, padx=5)

        # Hacer que la ventana emergente sea modal (bloquee el foco del resto de la aplicación)
        ventana_emergente.grab_set()
        ventana_emergente.focus_set()
        ventana_emergente.wait_window()