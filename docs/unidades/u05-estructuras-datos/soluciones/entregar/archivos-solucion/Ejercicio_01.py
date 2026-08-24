# Ejercicio 1
''' Muestra información del sistema operativo (sistema, versión, nodo y procesador) y almacena los datos en un diccionario. Crea una lista con los valores y muéstralos ordenados alfabéticamente.'''

import platform

sistema = {
    'Sistema': platform.system(),
    'Versión': platform.version(),
    'Nombre del nodo': platform.node(),
    'Procesador': platform.processor()
}

valores = sorted(sistema.values())

print("Valores del sistema ordenados:")
for valor in valores:
    print(valor)
