from tkinter import messagebox
from DB.dbmanager import dbManager

def obtener_productos():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT * FROM Producto"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados

def alta_productos(nombre,precio):
    exito=False
    db=dbManager()
    try:
        query="INSERT INTO producto (Nombre,Precio_Compra,Existencia) VALUES (%s,%s,%s)"
        values=(nombre,precio,0)
        db.cursor.execute(query,values)
        #Guardar cambios
        db.conn.commit()
        exito=True
        messagebox.showinfo("Registro exitoso", "Platillo registrado correctamente.")
    except Exception as error:
        messagebox.showerror("Error al registrar el platillo", error)
    db.close()
    return exito

def actualizar_producto(id_producto, nombre,precio_compra, existencia):
    exito=False
    db=dbManager()
    #Consulta SQL
    try:
        query="UPDATE producto SET Nombre=%s, Precio_Compra=%s, Existencia=%s WHERE ID_Producto=%s"
        values = (nombre, precio_compra,existencia, id_producto)
        db.cursor.execute(query, values)
        #guardar cambios en la base de datos
        db.conn.commit()
        exito=True
        messagebox.showinfo("Actualización exitosa", "Producto actualizado correctamente.")
    except Exception as error:
        messagebox.showerror("Error al actualizar los datos", error)
    
    db.close()
    return exito