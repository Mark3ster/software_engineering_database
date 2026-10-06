import sqlite3


def conectar():
    conexion = sqlite3.connect("preferencias.db")
    return conexion


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preferencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        clave TEXT NOT NULL,
        valor TEXT NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()


def guardar_preferencia(usuario_id, clave, valor):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO preferencias (usuario_id, clave, valor)
    VALUES (?, ?, ?)
    """, (usuario_id, clave, valor))

    conexion.commit()
    conexion.close()


def obtener_preferencias(usuario_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT clave, valor
    FROM preferencias
    WHERE usuario_id = ?
    """, (usuario_id,))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados

