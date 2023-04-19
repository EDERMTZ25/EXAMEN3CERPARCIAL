from tkinter import messagebox
import sqlite3


class ControladorBD:
    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion = sqlite3.connect("BDImportaciones.db")
        # print("Conectado con exito")
            return conexion
        except sqlite3.OperationalError:
            print("Fallo en la conexion")

    def ingresar(self, mercancia, pais):
        conx = self.conexionBD()
        cursor = conx.cursor()
        cursor.execute("insert into TB_Europa(mercancia, pais) values(?,?)", (mercancia, pais))
        conx.commit()
        conx.close()
        messagebox.showinfo("EXITO", "Se guardo la mercancia")

    def consultar(self, pais):
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            cursor.execute("select * from TB_Europa where pais = ?", (pais,))
            mercancia = cursor.fetchall()
            conx.close()
            return mercancia
        except:
            messagebox.showerror("ERROR", "No se encontro la mercancia")
            conx.close()
            return

    def eliminar(self, id):
        conx = self.conexionBD()
        cursor = conx.cursor()
        cursor.execute("delete from TB_Europa where IDImpo = ?", (id,))
        conx.commit()
        conx.close()
        messagebox.showinfo("EXITO", "Se elimino la mercancia")
