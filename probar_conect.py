import psycopg2
import getpass

def probar_conexion():
    try:
        # Datos de conexión
        usuario = input("Usuario: ")
        contraseña = getpass.getpass("Contraseña: ")
        nombre_basedatos = input("Ingrese el nombre de la base de datos: ")
        host = input("ingrese la direccion host de la base de datos: ")

        # Conexión a la base de datos
        conn = psycopg2.connect(
            dbname=nombre_basedatos,
            user=usuario,
            password=contraseña,
            host=host
        )

        # Ejecutar una consulta de prueba
        cur = conn.cursor()
        cur.execute("SELECT version()")
        version = cur.fetchone()
        print("Conexión exitosa. Versión de PostgreSQL:", version[0])

    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        # Cerrar la conexión
        if conn is not None:
            conn.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    probar_conexion()
