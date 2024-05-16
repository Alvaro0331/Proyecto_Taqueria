import tkinter as tk
from tkinter import END, messagebox, ttk
import mysql.connector
import subprocess

class dbManager:
    def __init__(self):
        self.user="root"
        self.password=""
        self.database="taqueria"
        self.host="localhost"
        self.conectar()
    
    def conectar(self):
        try:
            self.conn=mysql.connector.connect(host=self.host,user=self.user,passwd=self.password,database=self.database)
            self.cursor=self.conn.cursor()
            return True
        except mysql.connector.Error as error:
            messagebox.showerror("Error al conectar con la base de datos: ",error)
            
    
    def close(self):
        self.cursor.close()
        self.conn.close()
        
    def respaldarBD(self):
        try:
            with open("Respaldo_Taqueria.sql","w") as f:
                process=subprocess.Popen(["C:\\xampp\\mysql\\bin\\mysqldump", "-h", self.host, "-u", self.user, "-p" +self.password, "taqueria"], stdout=f)
                process.wait()
            messagebox.showinfo("Exito","Respaldo realizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al hacer el respaldo: {str(e)}")