from tkinter import messagebox
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