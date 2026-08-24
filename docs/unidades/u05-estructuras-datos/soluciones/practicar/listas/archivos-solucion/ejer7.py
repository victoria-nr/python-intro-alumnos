
lista1 = []
lista2 = []
   
print("Elementos para la lista 1")
for i in range(5):
    num = int(input(f"Número {i + 1}: "))
    lista1.append(num)

print("Elementos para la lista 2")
for i in range(5):
    num = int(input(f"Número {i + 1}: "))
    lista2.append(num)

# Unir las listas en una sola
resultado = lista1 + lista2 

print("\nLista resultado:", resultado)
