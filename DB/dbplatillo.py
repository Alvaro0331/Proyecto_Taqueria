from tkinter import messagebox
from DB.dbmanager import dbManager

def obtener_platillos():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT * FROM platillo"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados

def actualizar_platillo(id_platillo, nombre,descripcion):
    exito=False
    db=dbManager()
    #Consulta SQL
    try:
        query="UPDATE platillo SET nombre=%s, comentarios=%s WHERE ID_Platillo=%s"
        values = (nombre, descripcion, id_platillo)
        db.cursor.execute(query, values)
        #guardar cambios en la base de datos
        db.conn.commit()
        exito=True
        messagebox.showinfo("Actualización exitosa", "Platillo actualizado correctamente.")
    except Exception as error:
        messagebox.showerror("Error al actualizar los datos", error)
    
    db.close()
    return exito

def platillo_alta(nombre,comentario):
    exito=False
    db=dbManager()
    try:
        query="INSERT INTO platillo (Nombre,Comentarios) VALUES (%s,%s)"
        values=(nombre,comentario)
        db.cursor.execute(query,values)
        #Guardar cambios
        db.conn.commit()
        exito=True
        messagebox.showinfo("Registro exitoso", "Platillo registrado correctamente.")
    except Exception as error:
        messagebox.showerror("Error al registrar el platillo", error)
    db.close()
    return exito