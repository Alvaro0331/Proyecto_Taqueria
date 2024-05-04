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