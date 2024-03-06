import os
from collections import defaultdict
from PyPDF2 import PdfReader, PdfWriter

def get_mensura_name(filename):
    # Obtener el nombre de la mensura sin los números después del segundo guion
    parts = filename.split('-')
    return '-'.join(parts[:2])


def merge_pdfs(input_dir, output_dir):
    # Crear un diccionario para almacenar los archivos PDF de cada mensura
    mensura_pdfs = defaultdict(list)

    # Buscar todos los archivos PDF en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            # Obtener el nombre de la mensura sin los números después del primer guion
            mensura_name = get_mensura_name(filename)
            mensura_pdfs[mensura_name].append(os.path.join(input_dir, filename))

    # Fusionar los archivos PDF para cada mensura
    for mensura_name, pdf_files in mensura_pdfs.items():
        pdf_writer = PdfWriter()

        # Agregar cada página de los archivos PDF al escritor de PDF
        for pdf_file in pdf_files:
            pdf_reader = PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

        # Escribir el archivo PDF fusionado
        output_filename = os.path.join(output_dir, f'{mensura_name}.pdf')
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print(f'Se han fusionado los PDFs de la mensura {mensura_name} en {output_filename}.')

# Directorio de entrada que contiene los archivos PDF de las mensuras
input_directory = 'C:/Users/Admin/Desktop/pdf'

# Directorio de salida donde se guardarán los archivos PDF fusionados
output_directory = 'C:/Users/Admin/Desktop/pdf'

# Llamar a la función merge_pdfs
merge_pdfs(input_directory, output_directory)