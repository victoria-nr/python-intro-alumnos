# Calcular sueldo semanal preguntando las horas de cada día
horas_sem = 0

sueldo_hora = float(input("Introduce el sueldo por hora: "))

for dia in range(1, 7):
    horas = int(input(f"¿Cuántas horas has trabajado el día {dia}?: "))
    horas_sem += horas

sueldo_sem = sueldo_hora * horas_sem

print(f"Horas acumuladas en la semana: {horas_sem}")
print(f"Sueldo semanal: {sueldo_sem:.2f} euros")
