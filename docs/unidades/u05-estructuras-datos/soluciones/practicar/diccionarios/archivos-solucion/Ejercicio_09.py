# Ejercicio 9
'''Escribe un programa que lea 5 frases introducidas por el usuario
 y almacene en un diccionario cuántas veces aparece cada palabra. 
 Ignora mayúsculas/minúsculas.'''

conteo = {}
for _ in range(5):
    frase = input("Introduce una frase: ")
    for palabra in frase.lower().split():
        if palabra not in conteo:
            conteo[palabra]=1
        else:
            conteo[palabra]+=1

        #forma más avanzada de hacer lo anterior
        #conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)
