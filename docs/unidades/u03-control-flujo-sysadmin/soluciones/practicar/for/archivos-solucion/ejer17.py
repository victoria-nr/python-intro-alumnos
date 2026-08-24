
horas_acum = 0  

num_trab = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_hora = float(input("Sueldo por hora: "))

# Para cada trabajador
for trabajador in range(1, num_trab + 1):
    horas_trab = 0  
    dias = int(input(f"¿Cuántos días ha trabajado el trabajador {trabajador}?: "))

    # Para cada día
    for dia in range(1, dias + 1):
        horas = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador} el día {dia}?: "))
        horas_trab += horas 
   
    sueldo_semanal = horas_trab * sueldo_hora
    print(f"El trabajador {trabajador} tiene de sueldo {sueldo_semanal:.2f}")

    horas_acum += horas_trab

total_pago = horas_acum * sueldo_hora
print(f"El pago a los {num_trab} trabajadores es: {total_pago}")
