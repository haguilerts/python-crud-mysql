from bd_config import conectar
import re
from mysql.connector import Error

class Contacto:
    def __init__(self, nombre, apellido, telefono, email, id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    # -------------------
    # Método: Validar campos
    # -------------------
    def es_valido(self):
        errores = []

        if not self.nombre.isalpha():
            errores.append("Nombre: solo letras")
        if not self.apellido.isalpha():
            errores.append("Apellido: solo letras")
        if not self.telefono.isdigit():
            errores.append("Teléfono: solo números")
        if not re.match(r"^[\w\d]+@[\w\d]+\.\w{2,3}$", self.email):
            errores.append("Email: formato inválido")

        return errores

    # -------------------
    # Método: Guardar contacto
    # -------------------
    def guardar(self):
        errores = self.es_valido()
        if errores:
            return False, errores

        try:
            conn = conectar()
            cursor = conn.cursor()
            sql = "INSERT INTO contactos (nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s)"
            valores = (self.nombre, self.apellido, self.telefono, self.email)
            cursor.execute(sql, valores)
            conn.commit()
            conn.close()
            print("Contacto guardado con éxito")
            return True, None
        except Error as e:
            return False, [f"Error BD: {e}"]

    # -------------------
    # Método: Modificar contacto
    # -------------------
    def actualizar(self):
        if self.id is None:
            return False, ["ID del contacto es necesario para actualizar"]

        errores = self.es_valido()
        if errores:
            return False, errores

        try:
            conn = conectar()
            cursor = conn.cursor()
            sql = "UPDATE contactos SET nombre=%s, apellido=%s, telefono=%s, email=%s WHERE id=%s"
            valores = (self.nombre, self.apellido, self.telefono, self.email, self.id)
            cursor.execute(sql, valores)
            conn.commit()
            conn.close()
            print("Contacto actualizado con éxito")
            return True, None
        except Error as e:
            return False, [f"Error BD: {e}"]

    # -------------------
    # Método: Eliminar contacto
    # -------------------
    def eliminar(self):
        if self.id is None:
            return False, ["ID del contacto es necesario para eliminar"]

        try:
            conn = conectar()
            cursor = conn.cursor()
            sql = "DELETE FROM contactos WHERE id=%s"
            valores = (self.id,)
            cursor.execute(sql, valores)
            conn.commit()
            conn.close()
            print("Contacto eliminado con éxito")
            return True, None
        except Error as e:
            return False, [f"Error BD: {e}"]

    # -------------------
    # Método: Listar contactos
    # -------------------
    @staticmethod
    def listar():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contactos")
            resultados = cursor.fetchall()
            conn.close()
            return resultados
        except Error as e:
            print(f"Error al listar contactos: {e}")
            return []
