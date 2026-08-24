# Calcular sueldo semanal de cada trabajador y el total que paga la empresa
horas_total = 0  
num_trab = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_hora = float(input("Sueldo por hora: "))


for trabajador in range(1, num_trab + 1):
    horas_sem = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador}?: "))
    sueldo_semanal = horas_sem * sueldo_hora
    horas_total += horas_sem  
    print(f"El trabajador {trabajador} tiene de sueldo {sueldo_semanal:.2f}")

total_pago = horas_total * sueldo_hora
print(f"El pago a los {num_trab} trabajadores es: {total_pago:.2f}")
