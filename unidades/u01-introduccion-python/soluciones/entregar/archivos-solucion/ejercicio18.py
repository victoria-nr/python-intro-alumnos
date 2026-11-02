# Obtener las iniciales del nombre y los apellidos de una persona

# Solicitar el nombre y los apellidos
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

# Obtener las iniciales (primer carácter de cada cadena) y convertirlas a mayúsculas
iniciales = (nombre[0] + apellido1[0] + apellido2[0]).upper()

# Mostrar las iniciales
print(f"Las iniciales son: {iniciales}")
