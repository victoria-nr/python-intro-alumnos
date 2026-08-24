# Ejercicio 3: 
'''Pide al usuario 4 nombres de archivo o directorio. Usa la librería `pathlib` para determinar si existen y su tipo (fichero o directorio) y almacena esa información en un diccionario. Es decir, el diccionario debe contener para cada ruta si es archivo, directorio o si no existe.'''

from pathlib import Path
info = {}
for i in range(4):
    ruta = Path(input(f"Introduce la ruta {i+1}: "))
    if ruta.is_file():
        info[ruta] = 'Archivo'
    elif ruta.is_dir():
        info[ruta] = 'Directorio'
    else:
        info[ruta] = 'No existe'

for ruta, tipo in info.items():
    print(f"{ruta}: {tipo}")
