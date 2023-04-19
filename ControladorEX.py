import tkinter as tk
import ControladorEX

class CRUDMerch:
    def __init__(self, master):
        self.master = master
        self.master.title('CRUD MERCH')
        self.master.geometry('400x300')

        # Crear los widgets necesarios para la interfaz
        self.name_label = tk.Label(self.master, text='ID:')
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.master, text='Email:')
        self.email_label.grid(row=1, column=0, padx=5, pady=5)

        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.insert_button = tk.Button(self.master, text='Insertar', command=self.insert_data)
        self.insert_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.master, text='Eliminar', command=self.delete_data)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.view_button = tk.Button(self.master, text='Consultar', command=self.view_data)
        self.view_button.grid(row=3, column=0, padx=5, pady=5)

    def insert_data(self):
        # Obtener los valores ingresados en la interfaz
        name = self.name_entry.get()
        email = self.email_entry.get()

        # Llamar al método correspondiente en el controlador para insertar los valores en la base de datos
        ControladorEX.insert_data(name, email)

        # Limpiar los campos de la interfaz
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def delete_data(self):
        # Obtener el valor del campo de nombre ingresado en la interfaz
        name = self.name_entry.get()

        # Llamar al método correspondiente en el controlador para eliminar el registro correspondiente en la base de datos
        CRUDMerch.delete_data(name)

        # Limpiar los campos de la interfaz
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def view_data(self):
        # Llamar al método correspondiente en el controlador para obtener todos los registros de la base de datos
        rows = CRUDMerch.view_data()

        # Crear una ventana secundaria para mostrar los registros obtenidos
        top = tk.Toplevel(self.master)

        for i, row in enumerate(rows):
            # Crear etiquetas para mostrar los valores del registro actual
            name_label = tk.Label(top, text=row[0])
            
