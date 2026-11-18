# Solicitar información del libro
titulo = input("Título del libro: ")
autor = input("Autor: ")
año = input("Año de publicación: ")
genero = input("Género: ")

# Crear la cadena multilínea
informacion = f"""Título: {titulo}
Autor: {autor}
Año: {año}
Género: {genero}
"""

# Imprimir la información
print(informacion)
