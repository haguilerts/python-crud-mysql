from backend.BBDD.bd_config import conectar
from backend.poo.personas import Cliente

def crear_cliente(contacto_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (contacto_id) VALUES (%s)", (contacto_id,))
    conn.commit()
    cursor.close()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT clientes.id, contactos.nombre FROM clientes "
                   "JOIN contactos ON clientes.contacto_id = contactos.id")
    resultados = cursor.fetchall()
    clientes = [Cliente(id=r[0], nombre=r[1]) for r in resultados]
    cursor.close()
    conn.close()
    return clientes

def eliminar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_cliente(id_cliente, nuevo_contacto_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET contacto_id=%s WHERE id=%s", (nuevo_contacto_id, id_cliente))
    conn.commit()
    cursor.close()
    conn.close()
