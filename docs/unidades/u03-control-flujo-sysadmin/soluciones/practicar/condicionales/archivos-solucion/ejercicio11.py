# Programa para determinar el tipo de triángulo según sus lados

ladoA = float(input("Introduce la longitud del lado A: "))
ladoB = float(input("Introduce la longitud del lado B: "))
ladoC = float(input("Introduce la longitud del lado C: "))

#triángulo rectángulo (Pitágoras)
if (ladoA**2 + ladoB**2 == ladoC**2) or (ladoB**2 + ladoC**2 == ladoA**2) or (ladoC**2 + ladoA**2 == ladoB**2):
    print("Triángulo Rectángulo")


if ladoA == ladoB == ladoC:
    print("Triángulo Equilátero")

elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoC == ladoA):
    print("Triángulo Isósceles")

else:
    print("Triángulo Escaleno")
