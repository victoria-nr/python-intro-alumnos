# Calcular la distancia entre dos puntos en el plano

# Importar la función sqrt para calcular la raíz cuadrada
import math

# Solicitar las coordenadas del primer punto
x1 = int(input("Dime la coordenada x1 del punto 1: "))
y1 = int(input("Dime la coordenada y1 del punto 1: "))

# Solicitar las coordenadas del segundo punto
x2 = int(input("Dime la coordenada x2 del punto 2: "))
y2 = int(input("Dime la coordenada y2 del punto 2: "))

# Calcular la distancia entre los puntos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar la distancia
print(f"Distancia: {distancia:.2f}")
