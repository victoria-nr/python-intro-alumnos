# Ejercicio 4
'''Escribe un programa que solicite al usuario una palabra y devuelva su significado usando el siguiente diccionario:

diccionario = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}

*Nota: Debes controlar correctamente si el usuario introduce una palabra que no existe.*'''

diccionario = {
    'python': 'Lenguaje de programación',
    'algoritmo': 'Conjunto de instrucciones',
    'variable': 'Espacio de memoria para almacenar datos'
}
palabra = input("Introduce una palabra: ")
print(diccionario.get(palabra, "Palabra no encontrada"))
