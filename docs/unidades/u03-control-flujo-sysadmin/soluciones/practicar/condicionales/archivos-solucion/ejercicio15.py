# Programa para calcular el coste del autobús y el coste por alumno

num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))


coste_por_alumno = 0.0
coste_autobus = 0.0

if num_alumnos >= 100:
    coste_por_alumno = 65
elif num_alumnos >= 50:
    coste_por_alumno = 70
elif num_alumnos >= 30:
    coste_por_alumno = 95
elif num_alumnos > 0:  # Menos de 30 alumnos
    coste_por_alumno = 2850 / num_alumnos
else:
    print("El número de alumnos debe ser un valor positivo.")
    exit()

coste_autobus = num_alumnos * coste_por_alumno

print(f"El coste por alumno es {coste_por_alumno:.2f} euros.")
print(f"El coste del autobús es {coste_autobus:.2f} euros.")
