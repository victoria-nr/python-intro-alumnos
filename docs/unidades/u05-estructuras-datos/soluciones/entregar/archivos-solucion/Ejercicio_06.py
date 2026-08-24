# Ejercicio 6: 
'''Usa `shutil.disk_usage` para mostrar en un diccionario el espacio total, usado y libre en GB (redondeando a un decimal) de tres rutas del sistema que pedirás por teclado. Muestra el contenido del diccionario recorriendo sus elementos.'''
import shutil
import os
rutas = []
for _ in range(3):
    #una ruta puede ser '/', '/tmp', '/home', etc
    rutas.append(input("Introduce ruta: "))
    
uso_disco = {}

for ruta in rutas:
    if not os.path.exists(ruta):
        total, usado, libre = 0,0,0
    else:
        total, usado, libre = shutil.disk_usage(ruta)
    uso_disco[ruta] = {'total': round(total/1024**3,1), 'usado': round(usado/1024**3,1), 'libre': round(libre/1024**3,1)}

for ruta, datos in uso_disco.items():
    print(f"{ruta} -> Total: {datos['total']} GB, Usado: {datos['usado']} GB, Libre: {datos['libre']} GB")
