import tkinter as tk
from frontend.gui_clientes import ventana_clientes
from frontend.gui_contacto import ventana_contactos
from frontend.gui_producto import ventana_productos

def menu_principal():
    root = tk.Tk()
    root.title("Menú Principal")
    root.geometry("300x250")

    tk.Button(root, text="Gestionar Contactos", width=25, command=ventana_contactos).pack(pady=10)
    tk.Button(root, text="Gestionar Clientes", width=25, command=ventana_clientes).pack(pady=10)
    tk.Button(root, text="Gestionar Productos", width=25, command=ventana_productos).pack(pady=10)
    tk.Button(root, text="Salir", width=25, command=root.destroy).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    menu_principal()
