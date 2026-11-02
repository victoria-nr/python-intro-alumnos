# Solicitar una frase
frase = input("Escribe una frase: ")

# Reemplazar vocales con asteriscos
frase_modificada = frase.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')

# Mostrar resultados
print("Frase original:", frase)
print("Frase modificada:", frase_modificada)
