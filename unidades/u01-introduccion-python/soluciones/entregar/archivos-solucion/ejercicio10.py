# Calcular la nota final de un alumno en la materia de Algoritmos

# Solicitar las notas parciales
parcial1 = float(input("Dime la nota del parcial 1: "))
parcial2 = float(input("Dime la nota del parcial 2: "))
parcial3 = float(input("Dime la nota del parcial 3: "))

# Solicitar las notas del examen final y el trabajo final
examen = float(input("Dime la nota del examen: "))
trabajo = float(input("Dime la nota del trabajo: "))

# Calcular la nota final
nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + 0.3 * examen + 0.15 * trabajo

# Mostrar la nota final
print(f"Nota final: {nota:.2f}")
