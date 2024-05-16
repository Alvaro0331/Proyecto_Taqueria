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
    treeview.bind("<<TreeviewSelect>>", lambda event: detalles_facturas(treeview))
    
    # Crear un Frame para contener formulario
    frame_formulario = tk.Frame(tab)
    frame_formulario.pack(fill=tk.BOTH, expand=True)
    
    #widgets
    # Lista de opciones para el Combobox
    opciones = obtener_proveedores()
    proveedorLabel = tk.Label(frame_formulario, text="Proveedor:")
    proveedorLabel.grid(row=0, column=0, padx=2, pady=5)
    proveedorCombobox = ttk.Combobox(frame_formulario, values=opciones, state="readonly")
    proveedorCombobox.grid(row=0, column=1, padx=2, pady=5)
    # Boton para registrar nueva factura
    botonFacturaAlta = ttk.Button(frame_formulario, text="Nueva factura", command=lambda: validar_campos_alta(proveedorCombobox,treeview))
    botonFacturaAlta.grid(row=1, column=0, columnspan=2, padx=2, pady=10)

#Ventana para detalle de factura#
def detalles_facturas(treeview):
    # Obtener el registro seleccionado
    item = treeview.focus()

    # Obtener los detalles del registro seleccionado
    detalles = treeview.item(item, "values")
    
    if detalles:
        id_factura = detalles[0]  # Primer valor es el ID del empleado
        print("ID de la factura seleccionada:", id_factura)  # Imprimir el ID en la consola
        # Crear y configurar la ventana emergente
        ventana_emergente = tk.Toplevel()
        ventana_emergente.title("Detalles de factura")
        
        # Crear frame para el Treeview
        frame_treeview = tk.Frame(ventana_emergente)
        frame_treeview.pack(pady=10, fill="both", expand=True)

        # Crear el Treeview para mostrar los detalles de la comanda
        treeview_detalles = ttk.Treeview(ventana_emergente, columns=("ID_DetalleF", "Cantidad","FK_Producto", "FK_Ingrediente"), show="headings")
        treeview_detalles.heading("ID_DetalleF", text="ID Detalle")
        treeview_detalles.heading("Cantidad", text="Cantidad")
        treeview_detalles.heading("FK_Producto", text="FK Producto")
        treeview_detalles.heading("FK_Ingrediente", text="FK Ingrediente")
        
        # Agregar scrollbar vertical
        scrollbar_y = ttk.Scrollbar(ventana_emergente, orient="vertical", command=treeview_detalles.yview)
        scrollbar_y.pack(side="right", fill="y")
        treeview_detalles.configure(yscrollcommand=scrollbar_y.set)
        
        #Obtener los resultados de la consulta SQL
        resultados = obtener_detalle_factura(id_factura)

        # Agregar los resultados al treeview
        for resultado in resultados:
            treeview_detalles.insert("", tk.END, values=resultado)
        
        treeview_detalles.pack(fill=tk.BOTH, expand=True)
        
        ##Formulario para agregar productos al detalle##
        # Crear frame para el formulario de agregar productos
        frame_formulario = tk.Frame(ventana_emergente)
        frame_formulario.pack(pady=10)
        
        #Obtener ingredientes y productos disponibles
        ingredientes=lista_ingredientes()
        productos=lista_productos()

        # Campos del formulario
        lbl_producto = tk.Label(frame_formulario, text="Producto/Ingrediente:")
        lbl_producto.grid(row=0, column=0, padx=5)
        combo_producto = ttk.Combobox(frame_formulario, values=[f"{id_producto}: {nombre} ({tipo})" for id_producto, nombre, tipo in ingredientes + productos], state="readonly")
        combo_producto.grid(row=0, column=1, padx=5)
        combo_producto.config(values=[f"{id_producto}: {nombre} ({tipo})" for id_producto, nombre, tipo in ingredientes + productos],)
        lbl_cantidad = tk.Label(frame_formulario, text="Cantidad:")
        lbl_cantidad.grid(row=1, column=0, padx=5)        
        entry_cantidad = tk.Entry(frame_formulario)
        entry_cantidad.grid(row=1, column=1, padx=5)
        #Boton
        btn_agregar=tk.Button(frame_formulario,text="Agregar", command=lambda: validar_campos(combo_producto,entry_cantidad,id_factura, treeview,ventana_emergente))
        btn_agregar.grid(row=3, column=1, padx=5)

        # Hacer que la ventana emergente sea modal
        ventana_emergente.grab_set()
        ventana_emergente.focus_set()
        
        # Esperar hasta que la ventana se cierre y luego actualizar los datos de la comanda
        ventana_emergente.wait_window()
        
        # Actualizar los datos de la comanda en el treeview
        treeview.delete(*treeview.get_children())
        resultados = obtener_facturas()
        for resultado in resultados:
            treeview.insert("", tk.END, values=resultado)

##Validar campos para dar de alta factura
def validar_campos_alta(proveedorCombobox,treeview):
    proveedor=proveedorCombobox.get()
    if not proveedor:
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        alta_factura(proveedor)
        actualizar_contenido_facturas(treeview)

##Validar campos##
def validar_campos(combo_producto,entry_cantidad,id_factura, treeview,ventana_emergente):
    elementoSeleccionado=combo_producto.get()
    cantidad=entry_cantidad.get()
    
    if not elementoSeleccionado or not cantidad:
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        id_elemento, tipo_elemento = obtener_id_tipo_elemento(elementoSeleccionado)
        if id_elemento is not None and tipo_elemento is not None:
            exito=agregar_detalle_factura(id_elemento,tipo_elemento,cantidad,id_factura)
            
            # Verificar si la inserción fue exitosa
            if exito:
                # Actualizar el treeview con los nuevos datos
                treeview.delete(*treeview.get_children())
                resultados = obtener_detalle_factura(id_factura)
                for resultado in resultados:
                    treeview.insert("", tk.END, values=resultado)
                # Cerrar la ventana emergente
                ventana_emergente.destroy()
        else:
            messagebox.showerror("Error", "No se pudo obtener el ID y el tipo del elemento seleccionado.")

# Función para obtener el ID y el tipo del elemento seleccionado en el Combobox
def obtener_id_tipo_elemento(elementoSeleccionado):
    # Split para obtener el nombre y el tipo del elemento
    nombre_elemento, tipo_elemento = elementoSeleccionado.rsplit(" (", 1)

    # Split para obtener solo el ID del elemento
    id_elemento = nombre_elemento.split()[0]

    # Retornar el ID y el tipo del elemento
    return id_elemento, tipo_elemento[:-1]  # Eliminar el paréntesis del tipo


###Actualizar contenido###
def actualizar_contenido_facturas(treeview):
    # Limpiar el contenido existente en el Treeview
    for item in treeview.get_children():
        treeview.delete(item)

    # Obtener nuevas facturas de la base de datos
    nuevas_facturas = obtener_facturas()

    # Insertar las nuevas facturas en el Treeview
    for factura in nuevas_facturas:
        treeview.insert("", tk.END, values=factura)