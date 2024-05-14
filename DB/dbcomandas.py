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