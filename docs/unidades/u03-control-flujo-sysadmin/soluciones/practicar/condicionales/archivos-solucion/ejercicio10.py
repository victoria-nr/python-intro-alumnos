import math

# Algoritmo para clasificar la relación entre dos circunferencias

x1 = float(input("Dime coordenada x de la primera circunferencia: "))
y1 = float(input("Dime coordenada y de la primera circunferencia: "))
r1 = float(input("Dime el radio de la primera circunferencia: "))

x2 = float(input("Dime coordenada x de la segunda circunferencia: "))
y2 = float(input("Dime coordenada y de la segunda circunferencia: "))
r2 = float(input("Dime el radio de la segunda circunferencia: "))

# Calcular la distancia entre los centros
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distancia > (r1 + r2):
    print("Circunferencias exteriores")
elif distancia == (r1 + r2):
    print("Circunferencias tangentes exteriores")
elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
    print("Circunferencias secantes")
elif distancia == abs(r1 - r2):
    print("Circunferencias tangentes interiores")
elif distancia > 0 and distancia < abs(r1 - r2):
    print("Circunferencias interiores")
elif distancia == 0:
    print("Circunferencias concéntricas")
