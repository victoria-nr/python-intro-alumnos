
nombres = []
edades = []

while True:
    nombre = input("Introduce el nombre del alumno (o '*' para terminar): ")
    if nombre == "*":
        break
    edad = int(input("Introduce la edad del alumno: "))
    
    nombres.append(nombre)
    edades.append(edad)

print("\nAlumnos mayores de edad:")
for i in range(len(edades)):
    if edades[i] >= 18:
        print(f"{nombres[i]} ({edades[i]} años)")

# Encontrar la edad máxima
edad_maxima = max(edades)
print("\nAlumnos más mayores:")
for i in range(len(edades)):
    if edades[i] == edad_maxima:
        print(f"{nombres[i]} ({edades[i]} años)")