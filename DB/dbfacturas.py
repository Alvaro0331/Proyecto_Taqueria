import tkinter as tk
from tkinter import END,messagebox,ttk
from DB.dbmanager import dbManager

def obtener_facturas():
    # Instancia del dbManager
    db = dbManager()
    
    # Consulta SQL
    query = """
    SELECT f.Folio_Factura, f.Fecha, f.FK_Proveedor, p.Nombre AS Proveedor
    FROM factura_compra f
    JOIN proveedor p ON f.FK_Proveedor = p.ID_Proveedor
    """
    db.cursor.execute(query)
    
    # Obtener resultados de la búsqueda
    resultados = db.cursor.fetchall()
    
    # Cerrar conexión
    db.close()
    # Retornar resultados
    return resultados

def obtener_detalle_factura(id_factura):
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT ID_DetalleF, Cantidad, FK_Producto, FK_Ingredientes FROM detalle_factura WHERE FK_Factura_Compra = %s"
    values=(id_factura,)
    db.cursor.execute(query,values)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados

def lista_productos():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT ID_Producto, Nombre FROM producto"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    productos=db.cursor.fetchall()
    
    # Agregar tipo de elemento ("Producto") a cada tupla
    productos_con_tipo = [(id_producto, nombre, "Producto") for id_producto, nombre in productos]
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return productos_con_tipo

def lista_ingredientes():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT ID_Ingredientes, Nombre FROM ingredientes"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    ingredientes=db.cursor.fetchall()
    
    # Agregar tipo de elemento ("Ingrediente") a cada tupla
    ingredientes_con_tipo = [(id_ingrediente, nombre, "Ingredientes") for id_ingrediente, nombre in ingredientes]
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return ingredientes_con_tipo

def agregar_detalle_factura(id_elemento,tipo,cantidad,id_factura):
    exito = False
    db = dbManager()
    try:
        # Obtener el nombre de la columna de la llave foránea (FK_Producto o FK_Ingredientes)
        columna_fk = f"FK_{tipo}"
        
        # Consulta SQL para obtener el ID del elemento seleccionado (producto o ingrediente)
        query_id = f"SELECT ID_{tipo} FROM {tipo.lower()} WHERE ID_{tipo} = %s"
        db.cursor.execute(query_id, (id_elemento,))
        id_elemento_existente = db.cursor.fetchone()
        
        if id_elemento_existente:
            # Consulta SQL para insertar en la tabla detalle_factura
                query_insert = f"INSERT INTO detalle_factura (Cantidad,FK_Factura_Compra, Tipo, {columna_fk}) VALUES (%s, %s, %s, %s)"
                values_insert = (cantidad,id_factura,tipo,id_elemento)
                db.cursor.execute(query_insert, values_insert)
                # Guardar cambios
                db.conn.commit()
                exito = True
        else:
            messagebox.showerror("Error", f"No se encontró el {tipo} con el ID {id_elemento}.")
    except Exception as error:
        messagebox.showerror("Error al agregar detalle de comanda", error)
    finally:
        # Cerrar conexión
        db.close()
    return exito