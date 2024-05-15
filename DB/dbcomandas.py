import tkinter as tk
from tkinter import END,messagebox,ttk
from DB.dbmanager import dbManager

def obtener_comandas():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT * FROM comanda"
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


def agregar_detalle_comanda(id_elemento, tipo, cantidad, precio_venta):
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
            # Consulta SQL para insertar en la tabla detalle_comanda
            query_insert = "INSERT INTO detalle_comanda (Cantidad, Hora, Precio_Venta, Tipo, {}) VALUES (%s, CURTIME(), %s, %s, %s)".format(columna_fk)
            values = (cantidad, precio_venta, tipo, id_elemento)
            db.cursor.execute(query_insert, values)
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