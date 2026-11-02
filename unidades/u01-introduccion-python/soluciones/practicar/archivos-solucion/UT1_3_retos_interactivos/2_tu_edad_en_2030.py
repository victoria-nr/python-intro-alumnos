# 2 Tu edad en 2030
# Pide la edad actual al usuario.
# Calcula cuántos años tendrá en 2030 y muéstralo.

edad_texto = input("Introduce tu edad actual: ")
edad = int(edad_texto)

anio_actual = 2025
anio_objetivo = 2030

anios_que_pasan = anio_objetivo - anio_actual
edad_en_2030 = edad + anios_que_pasan

print("Tu edad en 2030 será:", edad_en_2030)