import PyPDF2
import os

def contar_paginas(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        return len(pdf_reader.pages)

# Directorio que contiene los archivos PDF
directorio_pdf = 'C:/Users/Admin/Desktop/escaneo'

# Obtener la lista de archivos PDF
archivos_pdf = [archivo for archivo in os.listdir(directorio_pdf) if archivo.endswith('.pdf')]

# Contar las páginas y sumar
total_paginas = sum(contar_paginas(os.path.join(directorio_pdf, pdf)) for pdf in archivos_pdf)

print(f'Total de páginas en {len(archivos_pdf)} archivos PDF: {total_paginas}')









