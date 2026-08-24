# Calcular el km en el que se encuentran 2 coches
km1 = 70
km2 = 150

for km in range(1000):
    pos1= km1 + km
    pos2= km2 - km

    if pos1 >= pos2:
        print("Se encuentran en el km:", pos1)
        break
