# Programa para determinar si un año es bisiesto

year = int(input("Introduce el año: "))

if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
    print("Año bisiesto.")
else:
    print("Año no bisiesto.")
