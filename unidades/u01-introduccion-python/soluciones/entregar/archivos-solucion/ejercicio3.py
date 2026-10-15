# Calcular la hipotenusa dados los catetos de un triángulo rectángulo

# Importar la función sqrt para calcular la raíz cuadrada
import math

# Solicitar los datos de entrada
cateto1 = float(input("Introduce el cateto 1: "))
cateto2 = float(input("Introduce el cateto 2: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Mostrar el resultado
print(f"La hipotenusa es {hipotenusa}")
