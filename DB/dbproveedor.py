from tkinter import messagebox
from DB.dbmanager import dbManager

def obtener_proveedores():
    #Instancia del dbManager
    db=dbManager()
    
    #Consulta SQL
    query="SELECT * FROM proveedor"
    db.cursor.execute(query)
    
    #Obtener resultados de la busqueda
    resultados=db.cursor.fetchall()
    
    #Cerrar conexion
    db.close()
    #Retornar resultados
    return resultados

def proveedor_alta(nombre,telefono):
    exito=False
    db=dbManager()
    try:
        query="INSERT INTO proveedor (Nombre,Telefono) VALUES (%s,%s)"
        values=(nombre,telefono)
        db.cursor.execute(query,values)
        #Guardar cambios
        db.conn.commit()
        exito=True
        messagebox.showinfo("Registro exitoso", "Proveedor registrado correctamente.")
    except Exception as error:
        messagebox.showerror("Error al registrar al mesero", error)
    db.close()
    return exito

def actualizar_proveedor(id_proveedor, nombre, telefono):
    exito=False
    db=dbManager()
    #Consulta SQL
    try:
        query="UPDATE proveedor SET Nombre=%s, Telefono=%s WHERE ID_Proveedor=%s"
        values=(nombre,telefono,id_proveedor)
        db.cursor.execute(query,values)
        #guardar cambios en la base de datos
        db.conn.commit()
        exito=True
        messagebox.showinfo("Actualización exitosa", "Proveedor modificado correctamente.")
    except Exception as error:
        messagebox.showerror("Error al actualizar los datos", error)
    db.close()
    return exito