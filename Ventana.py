import tkinter as tk
from tkinter import ttk
from Controlador import ControladorBD
from tkinter import messagebox

# Crear un objeto de la clase ControladorBD
controlador = ControladorBD()

#Funciones
def ingresar():
    mercancia = mercacia.get()
    pais = pais_ingresar.get()
    controlador.ingresar(mercancia, pais)

def consultar():
    pais = pais_consultar.get()
    mercancia = controlador.consultar(pais)
    if mercancia is None:
        texBus.delete(1.0, tk.END)  # Borra el contenido actual del widget
        texBus.insert(tk.END, "No se encontró mercancía para ese país")
    else:
        texBus.delete(1.0, tk.END)  # Borra el contenido actual del widget
        texBus.insert(tk.END, mercancia)


def eliminar():
    id = id_eliminar.get()
    controlador.eliminar(id)



Ventana = tk.Tk()
Ventana.title("Importaciones")
Ventana.geometry("400x400")

notebook = ttk.Notebook(Ventana)
notebook.pack(fill="both", expand=True)

panel1 = ttk.Frame(notebook)
notebook.add(panel1, text="Insertar")

panel2 = ttk.Frame(notebook)
notebook.add(panel2, text="Consultar")

panel3 = ttk.Frame(notebook)
notebook.add(panel3, text="Eliminar")


#Panel 1
#Labels
labelt1 = tk.Label(panel1, text="Insertar mercancia")
labelt1.pack(pady=10)

label1 = tk.Label(panel1, text="Mercancia")
label1.pack(pady=10)
mercacia = tk.StringVar()
entry1 = tk.Entry(panel1, textvariable=mercacia)
entry1.pack(pady=5)

label2 = tk.Label(panel1, text="Pais")
label2.pack(pady=10)
pais_ingresar = tk.StringVar()
entry2 = tk.Entry(panel1, textvariable=pais_ingresar)
entry2.pack(pady=5)

#Boton
boton1 = tk.Button(panel1, text="Ingresar", command=ingresar)
boton1.pack(pady=10)

#Panel 2
#Labels
labelt2 = tk.Label(panel2, text="Buscar por pais")
labelt2.pack(pady=10)

label3 = tk.Label(panel2, text="Pais")
label3.pack(pady=10)
pais_consultar = tk.StringVar()
entry3 = tk.Entry(panel2, textvariable=pais_consultar)
entry3.pack(pady=5)

#Boton
boton2 = tk.Button(panel2, text="Consultar", command=consultar)
boton2.pack(pady=10)

texBus = tk.Text(panel2, width=30, height=10)
texBus.pack(pady=10)

#Panel 3
#Labels
labelt3 = tk.Label(panel3, text="Eliminar por ID")
labelt3.pack(pady=10)

label4 = tk.Label(panel3, text="ID")
label4.pack(pady=10)
id_eliminar = tk.StringVar()
entry4 = tk.Entry(panel3, textvariable=id_eliminar)
entry4.pack(pady=5)

#Boton
boton3 = tk.Button(panel3, text="Eliminar", command=eliminar)
boton3.pack(pady=10)

Ventana.mainloop()








