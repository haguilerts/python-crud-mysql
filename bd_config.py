"""
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # como no tiene contraseña
            database="ispc",
            use_pure=True
        )

        if conn.is_connected():
            print("✅ Conexión a la base de datos exitosa")
            return conn
        else:
            print("⚠ No se pudo conectar a la base de datos")
            return None

    except Error as e:
        print("❌ Error al conectar a la base de datos:", e)
        return None

"""

import mysql.connector
from mysql.connector import Error

# Configuración de conexión (fácil de cambiar)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""  # Sin contraseña
DB_NAME = "ispc"

def conectar():
    """
    Función para conectarse a la base de datos MySQL.
    Devuelve el objeto de conexión si tiene éxito, o None si falla.
    """
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            use_pure=True
        )

        if conn.is_connected():
            print("✅ Conexión a la base de datos exitosa")
            return conn
        else:
            print("⚠ No se pudo conectar a la base de datos")
            return None

    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None
