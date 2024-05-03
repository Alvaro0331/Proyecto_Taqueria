from tkinter import messagebox
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

def actualizar_mesero(id_empleado, nombre, telefono, turno):
    exito=False
    db=dbManager()
    #Consulta SQL
    try:
        query="UPDATE mesero SET nombre=%s, telefono=%s, turno=%s WHERE ID_Mesero=%s"
        values = (nombre, telefono, turno, id_empleado)
        db.cursor.execute(query, values)
        #guardar cambios en la base de datos
        db.conn.commit()
        exito=True
        messagebox.showinfo("Actualización exitosa", "Los datos del empleado se actualizaron correctamente.")
    except Exception as error:
        messagebox.showerror("Error al actualizar los datos", error)
    
    db.close()
    return exito