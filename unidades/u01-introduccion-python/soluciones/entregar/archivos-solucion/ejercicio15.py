# Intercambiar los valores de dos variables y mostrarlos

# Solicitar los valores de las variables A y B
a = int(input("Introduce el valor de la variable A: "))
b = int(input("Introduce el valor de la variable B: "))

# Intercambiar los valores usando una variable auxiliar
aux = a
a = b
b = aux

# Se podría hacer también usando la siguiente expresión
# a, b = b, a

# Mostrar los nuevos valores de las variables
print(f"Nuevo valor de A: {a}")
print(f"Nuevo valor de B: {b}")
