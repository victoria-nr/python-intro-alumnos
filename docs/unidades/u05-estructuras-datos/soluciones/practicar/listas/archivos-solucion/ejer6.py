
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



num_mes = int(input("Introduce un número de mes (1-12): "))
while num_mes < 1 or num_mes > 12:
    print("Número de mes no válido. Debe estar entre 1 y 12.")
    num_mes = int(input("Introduce un número de mes (1-12): "))


nombre_mes = meses[num_mes - 1]
dias = dias_mes[num_mes - 1]
print(f"El mes {nombre_mes} tiene {dias} días.")

