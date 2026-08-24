# Ejercicio 10
'''Dado un diccionario con productos y su precio, escribe un programa 
que calcule el precio total de una compra solicitando al usuario qué 
productos desea y en qué cantidad mediante un bucle. El bucle terminará
cuando el usuario introduzca la palabra 'FIN'. Cuando el usuario escoja
un producto, imprime el desglose del producto, la cantidad, el precio
por unidad y precio total. Al finalizar, imprime el total de la compra.
Crea tú mismo el diccionario con al menos 4 pares producto-precio.'''

productos = {'pan': 0.8, 'leche': 1.2, 'huevos': 2.0, 'galletas': 2.5}
total = 0
while True:
    print(productos)
    prod = input("Escoge un producto (FIN para terminar): ")
    if prod == "FIN":
        break
    if prod in productos:
        cantidad = int(input(f"Cantidad de {prod}: "))
        subtotal = cantidad * productos[prod]
        total += subtotal
        print(f"{prod}: {cantidad} x {productos[prod]} = {subtotal:.2f}€")
    else:
        print("Producto no encontrado")
print(f"Total: {total:.2f}€")
