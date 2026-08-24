# Ejercicio 9
'''
Simula la gestión de la variable de entorno PATH, que contiene varias rutas separadas por : (dos puntos).
A partir de un string que representa un PATH, conviértelo en una lista, añade una nueva ruta al final (pídela por teclado), otra al inicio (pídela por teclado), y luego vuelve a unirlo en un solo string. Muestra el resultado final.
'''
ruta_path = "/usr/local/bin:/usr/bin:/bin"

rutas = ruta_path.split(":")

#"/opt/scripts"
#"/custom/bin"
rutas.append(input("Ruta para añadir al final: "))
rutas.insert(0, input("Ruta para añadir al inicio: "))


nuevo_path = ":".join(rutas)


print("Rutas individuales:")
for ruta in rutas:
    print("-", ruta)
print("\nNuevo PATH resultante:")
print(nuevo_path)
