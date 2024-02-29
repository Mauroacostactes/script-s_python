def login():
    # Base de datos ficticia de usuarios y contraseñas
    usuarios = {'usuario1': 'contrasena1', 'usuario2': 'contrasena2', 'usuario3': 'contrasena3'}

    intentos = 3  # Número de intentos permitidos

    while intentos > 0:
        usuario = input('Ingrese su nombre de usuario: ')
        contrasena = input('Ingrese su contraseña: ')

        # Verificar si el usuario y la contraseña coinciden
        if usuarios.get(usuario) == contrasena:
            print('Inicio de sesión exitoso. ¡Bienvenido, {}!'.format(usuario))
            break
        else:
            intentos -= 1
            print('Usuario o contraseña incorrectos. Intentos restantes: {}'.format(intentos))

    if intentos == 0:
        print('Número máximo de intentos alcanzado. Cierre del programa.')

if __name__ == "__main__":
    login()
