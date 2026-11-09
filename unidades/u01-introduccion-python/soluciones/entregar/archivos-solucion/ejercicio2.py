# Calcular el perímetro y área de un rectángulo dada su base y su altura.

# Solicitar los datos de entrada
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

# Calcular el perímetro y el área
perimetro = 2 * base + 2 * altura
area = base * altura

# Mostrar los resultados
print(f"El perímetro es {perimetro} y el área es {area}")
