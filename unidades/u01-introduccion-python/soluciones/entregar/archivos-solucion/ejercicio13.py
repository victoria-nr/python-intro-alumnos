# Calcular la raíz cuadrada y cúbica de un número

# Importar la función sqrt para calcular la raíz cuadrada
import math

# Solicitar el número
num = float(input("Dime el número: "))

# Calcular la raíz cuadrada
raiz_cuadrada = math.sqrt(num)

# Calcular la raíz cúbica (elevando a la potencia 1/3)
raiz_cubica = num ** (1/3)

# Mostrar las raíces
print(f"Raíz cuadrada: {raiz_cuadrada:.2f}")
print(f"Raíz cúbica: {raiz_cubica:.2f}")
