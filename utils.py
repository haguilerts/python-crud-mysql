import tkinter as tk
from tkinter import ttk, messagebox
from back.contacto import Contacto

# ---------------------------
# Funciones para Contactos
# ---------------------------
def agregar_contacto():
    abrir_formulario_contacto("Agregar")

def modificar_contacto():
    item = tabla_contactos.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecciona un contacto para modificar")
        return
    abrir_formulario_contacto("Modificar", tabla_contactos.item(item)["values"])

def eliminar_contacto():
    item = tabla_contactos.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecciona un contacto para eliminar")
        return
    confirm = messagebox.askyesno("Confirmar", "¿Desea eliminar el contacto seleccionado?")
    if confirm:
        c = Contacto(*tabla_contactos.item(item)["values"][1:], id=tabla_contactos.item(item)["values"][0])
        c.eliminar()
        listar_contactos()

def listar_contactos():
    resultados = Contacto.listar()
    tabla_contactos.delete(*tabla_contactos.get_children())
    for r in resultados:
        tabla_contactos.insert("", "end", values=r)

def abrir_formulario_contacto(accion, datos=None):
    form = tk.Toplevel(root)
    form.title(f"{accion} Contacto")
    form.geometry("500x350")
    tk.Label(form, text=f"{accion} Contacto", font=("Arial", 16, "bold")).pack(pady=10)

    labels = ["Nombre", "Apellido", "Teléfono", "Email"]
    entries = {}

    for i, lbl in enumerate(labels):
        tk.Label(form, text=f"{lbl}:", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
        entry = tk.Entry(form)
        entry.pack(padx=20, fill="x")
        entries[lbl.lower()] = entry

    if datos:
        entries["nombre"].insert(0, datos[1])
        entries["apellido"].insert(0, datos[2])
        entries["telefono"].insert(0, datos[3])
        entries["email"].insert(0, datos[4])

    def guardar():
        nombre = entries["nombre"].get().strip()
        apellido = entries["apellido"].get().strip()
        telefono = entries["telefono"].get().strip()
        email = entries["email"].get().strip()
        errores = []

        if not nombre.isalpha():
            errores.append("Nombre solo letras")
        if not apellido.isalpha():
            errores.append("Apellido solo letras")
        if not telefono.isdigit():
            errores.append("Teléfono solo números")
        if "@" not in email or not email.endswith(".com"):
            errores.append("Email inválido")

        if errores:
            messagebox.showerror("Error", "\n".join(errores))
            return

        if accion == "Agregar":
            c = Contacto(nombre, apellido, telefono, email)
            c.guardar()
        elif accion == "Modificar":
            c = Contacto(nombre, apellido, telefono, email, id=datos[0])
            c.actualizar()

        listar_contactos()
        form.destroy()

    def cancelar():
        form.destroy()

    frame_botones = tk.Frame(form)
    frame_botones.pack(pady=10)
    tk.Button(frame_botones, text="Guardar", bg="#4CAF50", fg="white", width=12, command=guardar).grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Cancelar", bg="#f44336", fg="white", width=12, command=cancelar).grid(row=0, column=1, padx=5)

# ---------------------------
# Funciones para Productos
# ---------------------------
def gestionar_productos():
    ventana_prod = tk.Toplevel(root)
    ventana_prod.title("Lista de Productos")
    ventana_prod.geometry("700x400")

    # Título
    tk.Label(ventana_prod, text="Lista de Productos", font=("Arial", 18, "bold")).pack(pady=10)

    # Tabla de productos
    tabla_prod = ttk.Treeview(ventana_prod, columns=("id", "nombre", "precio", "stock"), show="headings")
    tabla_prod.heading("id", text="ID")
    tabla_prod.heading("nombre", text="Nombre")
    tabla_prod.heading("precio", text="Precio")
    tabla_prod.heading("stock", text="Stock")
    tabla_prod.pack(fill="both", expand=True, padx=10, pady=10)

    frame_btn = tk.Frame(ventana_prod)
    frame_btn.pack(pady=10)

    def abrir_formulario_producto(accion, datos=None):
        form = tk.Toplevel(ventana_prod)
        form.title(f"{accion} Producto")
        form.geometry("400x300")
        tk.Label(form, text=f"{accion} Producto", font=("Arial", 16, "bold")).pack(pady=10)

        labels = ["Nombre", "Precio", "Stock"]
        entries = {}

        for lbl in labels:
            tk.Label(form, text=f"{lbl}:", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
            entry = tk.Entry(form)
            entry.pack(padx=20, fill="x")
            entries[lbl.lower()] = entry

        if datos:
            entries["nombre"].insert(0, datos[1])
            entries["precio"].insert(0, datos[2])
            entries["stock"].insert(0, datos[3])

        def guardar():
            nombre = entries["nombre"].get().strip()
            precio = entries["precio"].get().strip()
            stock = entries["stock"].get().strip()
            errores = []

            if not nombre.isalpha():
                errores.append("Nombre solo letras")
            if not precio.replace(".", "", 1).isdigit():
                errores.append("Precio solo números")
            if not stock.isdigit():
                errores.append("Stock solo números enteros")
            if errores:
                messagebox.showerror("Error", "\n".join(errores))
                return
            messagebox.showinfo("Éxito", f"{accion} realizado con éxito")
            form.destroy()

        def cancelar():
            form.destroy()

        frame_botones = tk.Frame(form)
        frame_botones.pack(pady=10)
        tk.Button(frame_botones, text="Guardar", bg="#4CAF50", fg="white", width=12, command=guardar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Cancelar", bg="#f44336", fg="white", width=12, command=cancelar).grid(row=0, column=1, padx=5)

    tk.Button(frame_btn, text="Agregar", bg="#4CAF50", fg="white", width=12, command=lambda: abrir_formulario_producto("Agregar")).grid(row=0, column=0, padx=5)
    tk.Button(frame_btn, text="Modificar", bg="#2196F3", fg="white", width=12, command=lambda: abrir_formulario_producto("Modificar", tabla_prod.item(tabla_prod.selection())["values"] if tabla_prod.selection() else None)).grid(row=0, column=1, padx=5)
    tk.Button(frame_btn, text="Eliminar", bg="#f44336", fg="white", width=12, command=lambda: tabla_prod.delete(tabla_prod.selection())).grid(row=0, column=2, padx=5)

# ---------------------------
# Ventana principal
# ---------------------------
root = tk.Tk()
root.title("Sistema de Contactos")
root.geometry("900x600")

# Título principal
tk.Label(root, text="Sistema de Contacto", font=("Arial", 20, "bold")).pack(pady=10)

# Botones de Contactos
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)
tk.Button(frame_buttons, text="Agregar Contacto", bg="#4CAF50", fg="white", width=15, command=agregar_contacto).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Modificar Contacto", bg="#2196F3", fg="white", width=15, command=modificar_contacto).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Eliminar Contacto", bg="#f44336", fg="white", width=15, command=eliminar_contacto).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Listar Contactos", bg="#FF9800", fg="white", width=15, command=listar_contactos).grid(row=0, column=3, padx=5)

# Tabla de Contactos
tabla_contactos = ttk.Treeview(root, columns=("id", "nombre", "apellido", "telefono", "email"), show="headings")
tabla_contactos.heading("id", text="ID")
tabla_contactos.heading("nombre", text="Nombre")
tabla_contactos.heading("apellido", text="Apellido")
tabla_contactos.heading("telefono", text="Teléfono")
tabla_contactos.heading("email", text="Email")
tabla_contactos.pack(fill="both", expand=True, padx=10, pady=10)

# Botón para Productos
tk.Button(root, text="Gestionar Productos", bg="#FF9800", fg="white", width=20, command=gestionar_productos).pack(pady=10)

# Iniciar la app
root.mainloop()
