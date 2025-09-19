from backend.BBDD.bd_config import conectar
from backend.poo.productos import Producto
from backend.poo.compras import Compra

# Crear compra
def crear_compra(cliente_id, producto_id, cantidad, total):
    db = conectar()
    if db is None:
        return
    cursor = db.cursor()
    sql = """
        INSERT INTO compras (cliente_id, producto_id, cantidad, total)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (cliente_id, producto_id, cantidad, total))
    db.commit()
    db.close()
    print("✅ Compra registrada correctamente")


# Listar compras (devuelve objetos Compra)
def listar_compras():
    db = conectar()
    if db is None:
        return []

    cursor = db.cursor(dictionary=True)
    sql = """
        SELECT com.id, p.nombre AS producto_nombre, com.cantidad, com.total
        FROM compras com
        JOIN productos p ON com.producto_id = p.id
        ORDER BY com.fecha DESC
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    db.close()

    compras = []
    for row in resultados:
        # Creamos un Producto solo con el nombre (los otros valores no interesan)
        producto = Producto(row["producto_nombre"], "", 0, 0)
        compra = Compra(producto, row["cantidad"], row["total"])
        compras.append(compra)

    return compras


# Buscar compra por ID
def obtener_compra(compra_id):
    db = conectar()
    if db is None:
        return None

    cursor = db.cursor(dictionary=True)
    sql = """
        SELECT com.id, p.nombre AS producto_nombre, com.cantidad, com.total
        FROM compras com
        JOIN productos p ON com.producto_id = p.id
        WHERE com.id = %s
    """
    cursor.execute(sql, (compra_id,))
    row = cursor.fetchone()
    db.close()

    if row:
        producto = Producto(row["producto_nombre"], "", 0, 0)
        return Compra(producto, row["cantidad"], row["total"])
    return None


# Actualizar compra
def actualizar_compra(compra_id, producto_id, cantidad, total):
    db = conectar()
    if db is None:
        return
    cursor = db.cursor()
    sql = """
        UPDATE compras
        SET producto_id = %s, cantidad = %s, total = %s
        WHERE id = %s
    """
    cursor.execute(sql, (producto_id, cantidad, total, compra_id))
    db.commit()
    db.close()
    print("✅ Compra actualizada correctamente")


# Eliminar compra
def eliminar_compra(compra_id):
    db = conectar()
    if db is None:
        return
    cursor = db.cursor()
    sql = "DELETE FROM compras WHERE id = %s"
    cursor.execute(sql, (compra_id,))
    db.commit()
    db.close()
    print("🗑 Compra eliminada correctamente")
