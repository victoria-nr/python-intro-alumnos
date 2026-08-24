# Ejercicio 4: 
'''Ejercicio 4: Usa `pathlib` para listar los archivos y carpetas del directorio actual y guarda esa información (si son archivo o directorio) en un diccionario, tal y como se ha hecho en el ejercicio anterior.'''

from pathlib import Path

ruta = Path('.')
elementos = list(ruta.iterdir())

info = {}
for e in elementos:
    if e.is_file():
        info[e.name] = 'Archivo'
    elif e.is_dir():
        info[e.name] = 'Directorio'

for nombre, tipo in info.items():
    print(f"{nombre}: {tipo}")
