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