import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from backend.crud import producto_crud

def ventana_productos():
    root = tk.Tk()
    root.title("Gestión de Productos")
    root.geometry("700x400")

    tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Descripción", "Precio", "Stock"), show="headings")
    for col in tabla["columns"]:
        tabla.heading(col, text=col)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Agregar", width=12, command=lambda: agregar_producto()).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Actualizar", width=12, command=lambda: actualizar_producto()).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Eliminar", width=12, command=lambda: eliminar_producto()).pack(side=tk.LEFT, padx=5)

    # Funciones
    def cargar_productos():
        for row in tabla.get_children():
            tabla.delete(row)
        productos = producto_crud.listar_productos()
        for p in productos:
            tabla.insert("", tk.END, values=(p.id, p.nombre, p.descripcion, p.precio, p.stock))

    def agregar_producto():
        nombre = simpledialog.askstring("Nombre", "Ingrese nombre:")
        descripcion = simpledialog.askstring("Descripción", "Ingrese descripción:")
        try:
            precio = float(simpledialog.askstring("Precio", "Ingrese precio:"))
            stock = int(simpledialog.askstring("Stock", "Ingrese stock:"))
        except:
            messagebox.showerror("Error", "Precio o Stock inválido")
            return
        if nombre:
            producto_crud.crear_producto(nombre, descripcion, precio, stock)
            messagebox.showinfo("Éxito", "Producto agregado")
            cargar_productos()

    def actualizar_producto():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un producto")
            return
        id_producto = tabla.item(item[0])["values"][0]
        nombre = simpledialog.askstring("Nombre", "Nuevo nombre:")
        descripcion = simpledialog.askstring("Descripción", "Nueva descripción:")
        try:
            precio = float(simpledialog.askstring("Precio", "Nuevo precio:"))
            stock = int(simpledialog.askstring("Stock", "Nuevo stock:"))
        except:
            messagebox.showerror("Error", "Precio o Stock inválido")
            return
        producto_crud.actualizar_producto(id_producto, nombre, descripcion, precio, stock)
        messagebox.showinfo("Éxito", "Producto actualizado")
        cargar_productos()

    def eliminar_producto():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un producto")
            return
        id_producto = tabla.item(item[0])["values"][0]
        producto_crud.eliminar_producto(id_producto)
        messagebox.showinfo("Éxito", "Producto eliminado")
        cargar_productos()

    cargar_productos()
    root.mainloop()
