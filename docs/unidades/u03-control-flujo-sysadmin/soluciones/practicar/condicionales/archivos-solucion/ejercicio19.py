# Programa para determinar el número de días de un mes

mes = int(input("Introduce el número de mes (1-12): "))

#if mes in [1, 3, 5, 7, 8, 10, 12]:
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("31 días")
elif mes == 2:
    print("28 o 29 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#elif mes in [4, 6, 9, 11]:
    print("30 días")
else:
    print("Mes incorrecto")
