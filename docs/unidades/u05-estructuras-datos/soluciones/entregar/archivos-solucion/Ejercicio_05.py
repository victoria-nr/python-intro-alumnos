# Ejercicio 5: 
'''Crea 3 nombres de carpeta que se situarán en el directorio actual en una lista y convierte a tipo `Path`. A continuación, para cada carpeta, si no existe, la creas y guarda en un diccionario si las carpetas fueron creadas o ya existían. Muestra el contenido del diccionario recorriendo sus elementos.'''
from pathlib import Path
carpetas = [Path('./logs'), Path('./data'), Path('./temp')]
estado = {}

for carpeta in carpetas:
    if not carpeta.exists():
        carpeta.mkdir()
        estado[carpeta] = 'Creada'
    else:
        estado[carpeta] = 'Ya existía'

for carpeta, e in estado.items():
    print(f"{carpeta}: {e}")
