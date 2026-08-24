# Pedir caracteres y decir si es vocal o no (terminar con espacio)

for _ in range(1000):
    car = input("Introduce un carácter: ")
    
    # Asegurarse de que el carácter es solo uno
    if len(car) != 1:
        print("Por favor, introduce solo un carácter.")
        continue
    # Otra forma de asegurarse que el carácter es solo uno
    # while True:
    #     car = input("Introduce un carácter: ")
    #     if len(car) == 1:
    #         break
    #     print("Por favor, introduce solo un carácter.")

    if car == " ":
        break
    
    if car.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
