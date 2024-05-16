import tkinter as tk
from tkinter import END,messagebox,ttk
from DB.dbmanager import dbManager

def obtener_comandas():
    #Instancia del dbManager
    db=dbManager()
    
    # Consulta SQL para unir las tablas y obtener la información del mesero
    query = """
    SELECT comanda.Numero_Folio, comanda.Fecha, comanda.FK_Mesa, comanda.Total_Pagar, mesero.Nombre AS Mesero
    FROM comanda
    JOIN mesa ON comanda.FK_Mesa = mesa.Numero_Mesa
    JOIN mesero ON mesa.FK_Mesero = mesero.ID_Mesero
    """
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados

def obtener_detalle_comanda(id_comanda):
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT ID_DetalleC, Cantidad, Hora, Precio_Venta, FK_Producto, FK_Platillo FROM detalle_comanda WHERE FK_Comanda = %s"
    values=(id_comanda,)
    db.cursor.execute(query,values)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados

def productos_disponibles():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT ID_Producto, Nombre FROM producto WHERE existencia > 0"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    productos=db.cursor.fetchall()
    
    # Agregar tipo de elemento ("Producto") a cada tupla
    productos_con_tipo = [(id_producto, nombre, "Producto") for id_producto, nombre in productos]
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return productos_con_tipo

def platillos_disponibles():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT ID_Platillo, Nombre FROM platillo"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    platillos=db.cursor.fetchall()
    
    # Agregar tipo de elemento ("Platillo") a cada tupla
    platillos_con_tipo = [(id_platillo, nombre, "Platillo") for id_platillo, nombre in platillos]
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return platillos_con_tipo


def agregar_detalle_comanda(id_elemento, tipo, cantidad, precio_venta,id_comanda):
    exito = False
    db = dbManager()
    try:
        # Obtener el nombre de la columna de la llave foránea (FK_Producto o FK_Platillo)
        columna_fk = f"FK_{tipo}"
        
        # Consulta SQL para obtener el ID del elemento seleccionado (producto o platillo)
        query_id = f"SELECT ID_{tipo} FROM {tipo.lower()} WHERE ID_{tipo} = %s"
        db.cursor.execute(query_id, (id_elemento,))
        id_elemento_existente = db.cursor.fetchone()
        
        if id_elemento_existente:
            # Consulta SQL para verificar si el producto/platillo ya está presente en el detalle de la comanda
            query_existencia = f"SELECT ID_DetalleC FROM detalle_comanda WHERE {columna_fk} = %s AND FK_Comanda = %s AND Tipo = %s"
            db.cursor.execute(query_existencia, (id_elemento, id_comanda, tipo))
            detalle_existente = db.cursor.fetchone()

            if detalle_existente:  # Si el producto/platillo ya está presente, actualizar la fila existente
                id_detalle_existente = detalle_existente[0]
                # Actualizar la cantidad y el precio de venta del producto/platillo existente
                query_update = "UPDATE detalle_comanda SET Cantidad = Cantidad + %s, Precio_Venta = %s WHERE ID_DetalleC = %s"
                values_update = (cantidad, precio_venta, id_detalle_existente)
                db.cursor.execute(query_update, values_update)
            else:  # Si el producto/platillo no está presente, insertar una nueva fila
                # Consulta SQL para insertar en la tabla detalle_comanda
                query_insert = f"INSERT INTO detalle_comanda (Cantidad, Hora, Precio_Venta, FK_Comanda, Tipo, {columna_fk}) VALUES (%s, CURTIME(), %s, %s, %s, %s)"
                values_insert = (cantidad, precio_venta, id_comanda, tipo, id_elemento)
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