# Programa que pide un intervalo y analiza los números introducidos por el usuario.

suma_dentro_intervalo = 0
cont_fuera_intervalo = 0
igual_limites = False

while True:
    lim_inf = int(input("Introduce el límite inferior del intervalo: "))
    lim_sup = int(input("Introduce el límite superior del intervalo: "))
    if lim_inf <= lim_sup:
        break
    else:
        print("ERROR: El límite inferior debe ser menor que el superior.")


num = int(input("Introduce un número (0 para salir): "))
while num != 0:
    if lim_inf < num < lim_sup: # Pertenece al intervalo
        suma_dentro_intervalo += num
    else:
        cont_fuera_intervalo += 1 # No pertenece al intervalo

    if num == lim_inf or num == lim_sup: # Número igual a alguno de los límites
        igual_limites = True


    num = int(input("Introduce un número (0 para salir): "))


print("La suma de los números dentro del intervalo es:", suma_dentro_intervalo)
print("La cantidad de números fuera del intervalo es:", cont_fuera_intervalo)
if igual_limites:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")

