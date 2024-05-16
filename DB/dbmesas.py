import tkinter as tk
from tkinter import END,messagebox,ttk
from DB.dbmanager import dbManager

def obtener_meseros():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT Nombre FROM mesero"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return [nombre[0] for nombre in resultados]

def alta_mesa(mesero,clientes):
    id_mesero=obtener_id_mesero(mesero)
    if id_mesero is None:
        print(f"No se encontró mesero con nombre {mesero}")
        return False
    db = dbManager()
    try:
        query = "INSERT INTO mesa (Numero_Clientes, FK_Mesero) VALUES (%s, %s)"
        values = (clientes, id_mesero)
        db.cursor.execute(query, values)
        db.conn.commit()
        asignar_comanda()
        messagebox.showinfo("Mesa abierta", "Para agregar pedidos dirijase al apartado de comandas")
        return True
    except Exception as error:
        print("Error al abrir mesa", error)
        return False
    finally:
        db.close()

def obtener_id_mesero(nombre_mesero):
    db = dbManager()
    try:
        query = "SELECT ID_Mesero FROM mesero WHERE Nombre = %s"
        db.cursor.execute(query, (nombre_mesero,))
        result = db.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except Exception as error:
        print("Error while fetching mesero ID", error)
    finally:
        db.close()

def asignar_comanda():
    # Instancia del dbManager
    db = dbManager()
    
    try:
        # Consulta SQL para obtener la última mesa creada
        query = "SELECT Numero_Mesa FROM mesa ORDER BY Numero_Mesa DESC LIMIT 1"
        db.cursor.execute(query)
        # Obtener el resultado de la búsqueda
        mesa = db.cursor.fetchone()
        
        if mesa:
            # Extraer el Numero_Mesa del resultado
            numero_mesa = mesa[0]
            try:
                # Consulta SQL para insertar una nueva comanda
                query_comanda = "INSERT INTO comanda (Fecha, FK_Mesa) VALUES (CURDATE(), %s)"
                values = (numero_mesa,)
                db.cursor.execute(query_comanda, values)
                # Guardar cambios
                db.conn.commit()
                return True
            except Exception as error:
                print("Error al crear la comanda:", error)
                return False
        else:
            print("No se encontró ninguna mesa.")
            return False
    except Exception as error:
        print("Error al obtener la última mesa creada:", error)
        return False
    finally:
        # Cerrar conexión
        db.close()