# Solicitar una oración y una palabra
oracion = input("Escribe una oración: ")
palabra = input("Escribe una palabra: ")

# Comprobar si la palabra está en la oración
esta_presente = palabra in oracion
print(f"¿La palabra '{palabra}' está en la oración? {esta_presente}")
