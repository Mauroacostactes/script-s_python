import psycopg2
import getpass
from psycopg2 import sql

def cambiar_contraseña():
    try:
        # Conexión a la base de datos como administrador
        admin_usuario = input("Usuario de administrador: ")
        admin_password = getpass.getpass("Contraseña de administrador: ")
        admin_dbname = input("Ingrese el nombre de la base de datos: ")
        admin_ip = input("ingrese la direccion host de la base de datos: ")
        conn = psycopg2.connect(
            dbname=admin_dbname,
            user=admin_usuario,
            password=admin_password,
            host=admin_ip
        )
        
        # Usuario a modificar
        usuario_a_modificar = input("Usuario a modificar: ")
        
        # Solicitar y verificar nueva contraseña
        while True:
            nueva_contraseña = getpass.getpass("Nueva contraseña: ")
            confirmar_contraseña = getpass.getpass("Confirmar contraseña: ")
            if nueva_contraseña == confirmar_contraseña:
                break
            else:
                print("Las contraseñas no coinciden. Inténtalo de nuevo.")

        # Creación del cursor
        cur = conn.cursor()
        
        # Modificación de la contraseña del usuario
        cur.execute(sql.SQL("ALTER USER {} WITH ENCRYPTED PASSWORD %s").format(sql.Identifier(usuario_a_modificar)), (nueva_contraseña,))
        
        # Confirmar cambios
        conn.commit()
        print("Contraseña modificada exitosamente.")
        
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        
    finally:
        # Cerrar la conexión
        if conn is not None:
            conn.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    cambiar_contraseña()
