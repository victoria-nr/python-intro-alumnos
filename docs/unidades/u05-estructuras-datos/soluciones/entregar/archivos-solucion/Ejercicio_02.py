# Ejercicio 2: 
'''Solicita por teclado 3 nombres de usuario mediante un bucle y almacénalos en una lista. A continuación, almacena sus home directory en un diccionario usando `os.path.expanduser`. Muestra el contenido del diccionario formateado.'''
import os

usuarios = []
for i in range(3):
    nombre = input(f"Nombre del usuario {i+1}: ")
    usuarios.append(nombre)

homes = {}
for usuario in usuarios:
    homes[usuario] = os.path.expanduser(f'~{usuario}')

print("Directorios home de usuarios:")
for usuario, ruta in homes.items():
    print(f"{usuario}: {ruta}")
