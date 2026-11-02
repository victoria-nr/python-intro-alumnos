# Calcular el precio final de una compra con un descuento del 15%

# Solicitar el precio de la compra
precio = float(input("Dime el precio: "))

# Calcular el precio final aplicando el descuento del 15%
precio_final = precio - precio * 0.15

# Mostrar el precio final
print(f"Precio final: {precio_final:.2f}")
