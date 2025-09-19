import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from backend.crud import contacto_crud

def ventana_contactos():
    root = tk.Tk()
    root.title("Gestión de Contactos")
    root.geometry("650x400")

    tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Apellido", "Teléfono", "Email"), show="headings")
    for col in tabla["columns"]:
        tabla.heading(col, text=col)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Agregar", width=12, command=lambda: agregar_contacto()).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Actualizar", width=12, command=lambda: actualizar_contacto()).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Eliminar", width=12, command=lambda: eliminar_contacto()).pack(side=tk.LEFT, padx=5)

    # Funciones
    def cargar_contactos():
        for row in tabla.get_children():
            tabla.delete(row)
        contactos = contacto_crud.listar_contactos()
        for c in contactos:
            tabla.insert("", tk.END, values=(c.id, c.nombre, c.apellido, c.telefono, c.email))

    def agregar_contacto():
        nombre = simpledialog.askstring("Nombre", "Ingrese nombre:")
        apellido = simpledialog.askstring("Apellido", "Ingrese apellido:")
        telefono = simpledialog.askstring("Teléfono", "Ingrese teléfono:")
        email = simpledialog.askstring("Email", "Ingrese email:")
        if nombre and apellido:
            contacto_crud.crear_contacto(nombre, apellido, telefono, email)
            messagebox.showinfo("Éxito", "Contacto agregado")
            cargar_contactos()

    def actualizar_contacto():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un contacto")
            return
        id_contacto = tabla.item(item[0])["values"][0]
        nombre = simpledialog.askstring("Nombre", "Nuevo nombre:")
        apellido = simpledialog.askstring("Apellido", "Nuevo apellido:")
        telefono = simpledialog.askstring("Teléfono", "Nuevo teléfono:")
        email = simpledialog.askstring("Email", "Nuevo email:")
        if nombre and apellido:
            contacto_crud.actualizar_contacto(id_contacto, nombre, apellido, telefono, email)
            messagebox.showinfo("Éxito", "Contacto actualizado")
            cargar_contactos()

    def eliminar_contacto():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un contacto")
            return
        id_contacto = tabla.item(item[0])["values"][0]
        contacto_crud.eliminar_contacto(id_contacto)
        messagebox.showinfo("Éxito", "Contacto eliminado")
        cargar_contactos()

    cargar_contactos()
    root.mainloop()
