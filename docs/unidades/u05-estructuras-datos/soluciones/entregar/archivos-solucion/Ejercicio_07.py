# Ejercicio 7: 
'''Usa la librería `pathlib` para listar los usuarios en `/home`. Crea un diccionario con su nombre y cuántos archivos tienen en su carpeta de usuario. Muestra el contenido del diccionario recorriendo sus elementos.'''
from pathlib import Path

##Se puede usar directorio alternativo dentro del propio home porque no os va a dejar acceder a los home de otros usuarios
usuarios = Path('/home').iterdir()
conteo_archivos = {}

for usuario in usuarios:
    if usuario.is_dir():
        archivos = list(usuario.iterdir())
        conteo_archivos[usuario] = len(archivos)
    

for usuario, cantidad in conteo_archivos.items():
    print(f"{usuario}: {cantidad} archivos")
