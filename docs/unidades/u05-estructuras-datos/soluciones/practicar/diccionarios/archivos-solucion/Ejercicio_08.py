# Ejercicio 8
'''Dado un diccionario con nombres de personas como claves y su edad
 como valores, muestra el nombre de la persona más joven. Crea tú mismo
   el diccionario con al menos 3 pares clave-valor.'''

personas = {'Juan': 30, 'Ana': 25, 'Luis': 28}


min_persona = None
min_edad = None

# Recorremos el diccionario
for nombre in personas:
    edad = personas[nombre]
    if min_edad is None or edad < min_edad:
        min_edad = edad
        min_persona = nombre

# Mostramos el resultado
print("La persona más joven es", min_persona, "con", min_edad, "años.")

#solución avanzada
#joven = min(personas, key=personas.get)
#print(f"La persona más joven es {joven} con {personas[joven]} años.")
