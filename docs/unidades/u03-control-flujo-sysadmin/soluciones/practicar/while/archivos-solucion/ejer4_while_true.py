# Pedir caracteres y decir si es vocal o no (terminar con espacio)

while True:
    car = input("Introduce un carácter: ")
    
    # Asegurarse de que el carácter es solo uno
    if len(car) != 1:
        print("Por favor, introduce solo un carácter.")
        continue
    
    if car == " ":
        break
    
    if car.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
