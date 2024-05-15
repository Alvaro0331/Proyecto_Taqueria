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
        lbl_producto = tk.Label(frame_formulario, text="Producto/Platillo:")
        lbl_producto.grid(row=0, column=0, padx=5)
        combo_producto = ttk.Combobox(frame_formulario, values=[f"{id_producto}: {nombre} ({tipo})" for id_producto, nombre, tipo in productos + platillos], state="readonly")
        combo_producto.grid(row=0, column=1, padx=5)
        combo_producto.config(values=[f"{id_producto}: {nombre} ({tipo})" for id_producto, nombre, tipo in productos + platillos],)
        lbl_cantidad = tk.Label(frame_formulario, text="Cantidad:")
        lbl_cantidad.grid(row=1, column=0, padx=5)        
        entry_cantidad = tk.Entry(frame_formulario)
        entry_cantidad.grid(row=1, column=1, padx=5)
        lbl_precio=tk.Label(frame_formulario, text="Precio de venta")
        lbl_precio.grid(row=2, column=0,padx=5)
        entry_precio=tk.Entry(frame_formulario)
        entry_precio.grid(row=2, column=1,padx=5)
        #Boton
        btn_agregar=tk.Button(frame_formulario,text="Agregar", command=lambda: validar_campos(combo_producto,entry_cantidad,entry_precio,id_comanda, treeview,ventana_emergente))
        btn_agregar.grid(row=3, column=1, padx=5)

        # Hacer que la ventana emergente sea modal
        ventana_emergente.grab_set()
        ventana_emergente.focus_set()
        
        # Esperar hasta que la ventana se cierre y luego actualizar los datos de la comanda
        ventana_emergente.wait_window()
        
        # Actualizar los datos de la comanda en el treeview
        treeview.delete(*treeview.get_children())
        resultados = obtener_comandas()
        for resultado in resultados:
            treeview.insert("", tk.END, values=resultado)
        

##Validar campos##
def validar_campos(combo_producto,entry_cantidad,entry_precio,id_comanda, treeview,ventana_emergente):
    elementoSeleccionado=combo_producto.get()
    cantidad=entry_cantidad.get()
    precio=entry_precio.get()
    
    if not elementoSeleccionado or not cantidad or not precio:
        messagebox.showerror("Error", "Faltan campos por llenar.")
    else:
        id_elemento, tipo_elemento = obtener_id_tipo_elemento(elementoSeleccionado)
        if id_elemento is not None and tipo_elemento is not None:
            print("ID del elemento:", id_elemento)
            print("Tipo del elemento:", tipo_elemento)
            print("Cantidad:", cantidad)
            print("Precio de venta:", precio)
            print("Id de la comanda:",id_comanda)
            exito=agregar_detalle_comanda(id_elemento,tipo_elemento,cantidad,precio,id_comanda)
            
            # Verificar si la inserción fue exitosa
            if exito:
                # Actualizar el treeview con los nuevos datos
                treeview.delete(*treeview.get_children())
                resultados = obtener_detalle_comanda(id_comanda)
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