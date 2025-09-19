from backend.BBDD.bd_config import conectar
from backend.poo.productos import Producto

# Crear producto
def crear_producto(nombre, descripcion, precio, stock):
    db = conectar()
    if db is None:
        return
    cursor = db.cursor()
    sql = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, descripcion, precio, stock))
    db.commit()
    db.close()
    print("✅ Producto registrado correctamente")


# Listar productos (devuelve objetos Producto)
def listar_productos():
    db = conectar()
    if db is None:
        return []

    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM productos ORDER BY nombre ASC"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    db.close()

    productos = []
    for row in resultados:
        producto = Producto(row["nombre"], row["descripcion"], row["precio"], row["stock"])
        productos.append(producto)

    return productos


# Buscar producto por ID
def obtener_producto(producto_id):
    db = conectar()
    if db is None:
        return None

    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM productos WHERE id = %s"
    cursor.execute(sql, (producto_id,))
    row = cursor.fetchone()
    db.close()

    if row:
        return Producto(row["nombre"], row["descripcion"], row["precio"], row["stock"])
    return None


# Actualizar producto
def actualizar_producto(producto_id, nombre, descripcion, precio, stock):
    db = conectar()
    if db is None:
        return
    cursor = db.cursor()
    sql = """
        UPDATE productos
        SET nombre = %s, descripcion = %s, precio = %s, stock = %s
        WHERE id = %s
    """
    cursor.execute(sql, (nombre, descripcion, precio, stock, producto_id))
    db.commit()
    db.close()
    print("✅ Producto actualizado correctamente")


# Eliminar producto
def eliminar_producto(producto_id):
    db = conectar()
    if db is None:
        return
    cursor = db.cursor()
    sql = "DELETE FROM productos WHERE id = %s"
    cursor.execute(sql, (producto_id,))
    db.commit()
    db.close()
    print("🗑 Producto eliminado correctamente")
