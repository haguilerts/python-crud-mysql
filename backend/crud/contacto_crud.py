from backend.BBDD.bd_config import conectar
from backend.poo.personas import Contacto

def crear_contacto(nombre, apellido, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contactos (nombre, apellido, telefono, email) VALUES (%s,%s,%s,%s)",
                   (nombre, apellido, telefono, email))
    conn.commit()
    cursor.close()
    conn.close()

def listar_contactos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, telefono, email FROM contactos")
    resultados = cursor.fetchall()
    contactos = [Contacto(id=r[0], nombre=r[1], apellido=r[2], telefono=r[3], email=r[4]) for r in resultados]
    cursor.close()
    conn.close()
    return contactos

def eliminar_contacto(id_contacto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE id=%s", (id_contacto,))
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_contacto(id_contacto, nombre, apellido, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE contactos SET nombre=%s, apellido=%s, telefono=%s, email=%s WHERE id=%s",
                   (nombre, apellido, telefono, email, id_contacto))
    conn.commit()
    cursor.close()
    conn.close()
