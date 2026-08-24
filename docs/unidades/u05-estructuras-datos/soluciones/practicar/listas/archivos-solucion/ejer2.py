
lista_original = []

for i in range(5):
    cadena = input(f"Introduce la cadena {i + 1}: ")
    lista_original.append(cadena)

lista_invertida = lista_original[::-1]

print("\nLista invertida:")
for cadena in lista_invertida:
    print(cadena)
