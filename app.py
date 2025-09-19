import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from contacto import Contacto

# ---------------------------
# Funciones de la ventana principal
# ---------------------------

def refrescar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    contactos = Contacto.listar()
    for c in contactos:
        tabla.insert("", "end", values=c)
    ajustar_columnas()

def abrir_formulario(contacto=None):
    form = tk.Toplevel(root)
    form.title("Agregar Contacto" if contacto is None else "Modificar Contacto")
    form.geometry("500x400")
    form.grab_set()

    tk.Label(form, text="LISTA DE USUARIOS", font=("Arial", 18, "bold")).pack(pady=10)

    entries = {}
    labels = [("Nombre", "nombre"), ("Apellido", "apellido"), ("Teléfono", "telefono"), ("Email", "email")]
    for text, key in labels:
        tk.Label(form, text=text, font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
        e = tk.Entry(form, width=40)
        e.pack(padx=20, pady=5)
        entries[key] = e

    if contacto:
        entries["nombre"].insert(0, contacto[1])
        entries["apellido"].insert(0, contacto[2])
        entries["telefono"].insert(0, contacto[3])
        entries["email"].insert(0, contacto[4])

    def guardar_cambios():
        # Resetear colores antes de validar
        for key in entries:
            entries[key].config(bg="white")

        nuevo_nombre = entries["nombre"].get().strip()
        nuevo_apellido = entries["apellido"].get().strip()
        nuevo_telefono = entries["telefono"].get().strip()
        nuevo_email = entries["email"].get().strip()

        c = Contacto(nuevo_nombre, nuevo_apellido, nuevo_telefono, nuevo_email, id=contacto[0] if contacto else None)
        success, errores = c.guardar() if contacto is None else c.actualizar()

        if errores:
            # Pintar de rosado los campos con error
            for err in errores:
                if "Nombre" in err:
                    entries["nombre"].config(bg="#ffcccc")
                if "Apellido" in err:
                    entries["apellido"].config(bg="#ffcccc")
                if "Teléfono" in err:
                    entries["telefono"].config(bg="#ffcccc")
                if "Email" in err:
                    entries["email"].config(bg="#ffcccc")

            # Mostrar cartel emergente con errores
            messagebox.showerror("Error", "\n".join(errores))
        else:
            refrescar_tabla()
            form.destroy()
            messagebox.showinfo("Éxito", "Contacto guardado correctamente" if contacto is None else "Contacto actualizado correctamente")

    btn_frame = tk.Frame(form)
    btn_frame.pack(pady=15)
    tk.Button(btn_frame, text="Guardar", width=12, bg="#4CAF50", fg="white", command=guardar_cambios).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Cancelar", width=12, bg="#f44336", fg="white", command=form.destroy).grid(row=0, column=1, padx=10)

def seleccionar_contacto(event=None):
    selected = tabla.selection()
    if selected:
        item = tabla.item(selected[0])
        abrir_formulario(contacto=item["values"])

def eliminar_contacto():
    selected = tabla.selection()
    if not selected:
        messagebox.showwarning("Aviso", "Seleccione un contacto para eliminar")
        return
    item = tabla.item(selected[0])
    c = Contacto(*item["values"][1:], id=item["values"][0])
    success, errores = c.eliminar()
    if errores:
        messagebox.showerror("Error", "; ".join(errores))
    else:
        refrescar_tabla()
        messagebox.showinfo("Éxito", "Contacto eliminado correctamente")

# ---------------------------
# Ventana principal
# ---------------------------
root = tk.Tk()
root.title("SISTEMA DE CONTACTOS")
root.geometry("700x500")

tk.Label(root, text="SISTEMA DE CONTACTOS", font=("Arial", 20, "bold")).pack(pady=10)

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Agregar", width=12, bg="#2196F3", fg="white", command=lambda: abrir_formulario()).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Modificar", width=12, bg="#FFC107", fg="white", command=lambda: seleccionar_contacto()).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Eliminar", width=12, bg="#f44336", fg="white", command=eliminar_contacto).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Mostrar", width=12, bg="#4CAF50", fg="white", command=refrescar_tabla).grid(row=0, column=3, padx=5)

# Tabla
frame_tabla = tk.Frame(root)
frame_tabla.pack(pady=10, fill="both", expand=True)

tabla = ttk.Treeview(frame_tabla, columns=("id", "nombre", "apellido", "telefono", "email"), show="headings")
tabla.heading("id", text="ID")
tabla.heading("nombre", text="Nombre")
tabla.heading("apellido", text="Apellido")
tabla.heading("telefono", text="Teléfono")
tabla.heading("email", text="Email")
tabla.pack(fill="both", expand=True)

# Ajustar columnas
def ajustar_columnas():
    tabla.update_idletasks()
    for col in tabla["columns"]:
        if col == "id":
            tabla.column(col, width=50, anchor="center")
        else:
            tabla.column(col, width=150, anchor="w")

tabla.bind("<Double-1>", seleccionar_contacto)

# Inicializar tabla
refrescar_tabla()

# Iniciar app
root.mainloop()
