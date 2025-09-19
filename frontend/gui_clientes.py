import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from backend.crud import cliente_crud, contacto_crud

def ventana_clientes():
    root = tk.Tk()
    root.title("Gestión de Clientes")
    root.geometry("600x400")

    tabla = ttk.Treeview(root, columns=("ID", "Nombre"), show="headings")
    tabla.heading("ID", text="ID Cliente")
    tabla.heading("Nombre", text="Nombre Contacto")
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Agregar Cliente", width=15, command=lambda: agregar_cliente()).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Eliminar Cliente", width=15, command=lambda: eliminar_cliente()).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Actualizar Cliente", width=15, command=lambda: actualizar_cliente()).pack(side=tk.LEFT, padx=5)

    def cargar_clientes():
        for row in tabla.get_children():
            tabla.delete(row)
        clientes = cliente_crud.listar_clientes()
        for c in clientes:
            tabla.insert("", tk.END, values=(c.id, c.nombre))

    def agregar_cliente():
        contactos = contacto_crud.listar_contactos()
        if not contactos:
            messagebox.showwarning("Aviso", "No hay contactos disponibles")
            return
        ids = [f"{idx+1} - {c.nombre} {c.apellido}" for idx, c in enumerate(contactos)]
        seleccion = simpledialog.askinteger("Seleccionar contacto",
                                            "Ingrese el número del contacto:\n" + "\n".join(ids))
        if seleccion and 1 <= seleccion <= len(contactos):
            cliente_crud.crear_cliente(contactos[seleccion-1].id)
            messagebox.showinfo("Éxito", "Cliente creado")
            cargar_clientes()
        else:
            messagebox.showerror("Error", "Selección inválida")

    def eliminar_cliente():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un cliente")
            return
        id_cliente = tabla.item(item[0])["values"][0]
        cliente_crud.eliminar_cliente(id_cliente)
        messagebox.showinfo("Éxito", "Cliente eliminado")
        cargar_clientes()

    def actualizar_cliente():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un cliente")
            return
        id_cliente = tabla.item(item[0])["values"][0]

        contactos = contacto_crud.listar_contactos()
        if not contactos:
            messagebox.showwarning("Aviso", "No hay contactos disponibles")
            return
        ids = [f"{idx+1} - {c.nombre} {c.apellido}" for idx, c in enumerate(contactos)]
        seleccion = simpledialog.askinteger("Seleccionar contacto",
                                            "Ingrese el número del nuevo contacto:\n" + "\n".join(ids))
        if seleccion and 1 <= seleccion <= len(contactos):
            cliente_crud.actualizar_cliente(id_cliente, contactos[seleccion-1].id)
            messagebox.showinfo("Éxito", "Cliente actualizado")
            cargar_clientes()
        else:
            messagebox.showerror("Error", "Selección inválida")

    cargar_clientes()
    root.mainloop()
