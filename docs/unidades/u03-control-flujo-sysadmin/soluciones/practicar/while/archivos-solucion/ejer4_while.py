
# Pedir caracteres y decir si es vocal o no (terminar con espacio)
car = ""

while len(car) != 1: # Asegurarse de que el carácter es solo uno
    car = input("Introduce un carácter: ")

while car != " ":
    if car.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
    
    car = ""
    while len(car) != 1:
        car = input("Introduce un carácter: ")
