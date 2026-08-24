# Algoritmo para determinar la aceptación según nota, edad y sexo

nota = int(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ").upper()

if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("Aceptada")
    elif sexo == "M":
        print("Posible")
    else:
        print("No Aceptada")
else:
    print("No Aceptada")
