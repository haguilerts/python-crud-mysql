from backend.poo.productos import Producto

# Clase Compra
class Compra:
    def __init__(self, cliente):
        self.cliente = cliente      # objeto Cliente
        self.items = []             # lista de diccionarios {"producto": Producto, "cantidad": int, "total": float}

    # Agrega un producto a la compra
    def agregar_producto(self, producto, cantidad):
        self.items.append({
            "producto": producto,
            "cantidad": cantidad,
            "total": producto.precio * cantidad
        })

    # Calcula el total de la compra
    def total_compra(self):
        return sum(item["total"] for item in self.items)

    # Muestra detalle de la compra
    def mostrar_compra(self):
        detalle = [f"{i['producto'].nombre} x{i['cantidad']} = {i['total']}" for i in self.items]
        return f"Cliente: {self.cliente.nombre}\n" + "\n".join(detalle) + f"\nTotal: {self.total_compra()}"
