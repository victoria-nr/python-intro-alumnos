# Calcular la nota final de un estudiante basada en sus respuestas

# Solicitar la cantidad de respuestas correctas, incorrectas y en blanco
correctas = int(input("Dime la cantidad de respuestas correctas: "))
incorrectas = int(input("Dime la cantidad de respuestas incorrectas: "))
# Las respuestas en blanco no afectan el cálculo, por lo que no las pedimos

# Calcular los puntos obtenidos
puntos = correctas * 5 + incorrectas * (-1)

# Mostrar los puntos finales
print(f"Puntos: {puntos}")
