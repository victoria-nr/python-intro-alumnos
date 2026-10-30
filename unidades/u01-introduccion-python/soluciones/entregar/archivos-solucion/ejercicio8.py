# Calcular el sueldo total de un vendedor con comisiones por ventas

# Solicitar el sueldo base
sueldo_base = float(input("Dime el sueldo base: "))

# Solicitar los valores de las tres ventas
venta1 = float(input("Dime el precio de la venta 1: "))
venta2 = float(input("Dime el precio de la venta 2: "))
venta3 = float(input("Dime el precio de la venta 3: "))

# Calcular la comisión (10% de cada venta)
comision = venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1

# Calcular el sueldo total
sueldo_total = sueldo_base + comision

# Mostrar los resultados
print(f"Comisión por ventas: {comision:.2f}")
print(f"Sueldo total: {sueldo_total:.2f}")
