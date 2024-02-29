import os
import hashlib
import sys

# Función para calcular el hash de un archivo
def calcular_hash(nombre_archivo, tamaño_bloque=65536):
    sha1 = hashlib.sha1()
    with open(nombre_archivo, 'rb') as archivo:
        while True:
            data = archivo.read(tamaño_bloque)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

# Carpeta a verificar
carpeta = input("Ingrese la ruta de la carpeta a verificar: ")

# Diccionario para almacenar los archivos y sus hashes
archivos = {}

# Recorre la carpeta y calcula los hashes de los archivos
for directorio, subdirectorios, archivos_en_dir in os.walk(carpeta):
    for archivo in archivos_en_dir:
        ruta_completa = os.path.join(directorio, archivo)
        hash_archivo = calcular_hash(ruta_completa)
        if hash_archivo in archivos:
            archivos[hash_archivo].append(ruta_completa)
        else:
            archivos[hash_archivo] = [ruta_completa]

# Encuentra y muestra los archivos duplicados
for hash_archivo, rutas in archivos.items():
    if len(rutas) > 1:
        print(f'Archivos duplicados con hash {hash_archivo}:')
        for ruta in rutas:
            print(f'- {ruta}')
        
        # Pregunta al usuario si desea eliminar duplicados
        decision = input("¿Desea eliminar los duplicados? (Sí/No): ").lower()
        
        if decision == "si":
            # Mantén un original y elimina duplicados
            original = rutas[-1]
            duplicados = rutas[:-1]
            for duplicado in duplicados:
                os.remove(duplicado)
                print(f'Archivo duplicado eliminado: {duplicado}')
            print(f'Se conservó el archivo original: {original}')
        else:
            print('No se eliminaron archivos duplicados.')

# Si no hay archivos duplicados
if not archivos:
    print("No se encontraron archivos duplicados en la carpeta.")
