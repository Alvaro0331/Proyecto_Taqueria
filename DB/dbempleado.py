from DB.dbmanager import dbManager

def obtener_meseros():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT * FROM mesero"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados
