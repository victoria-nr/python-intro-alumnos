
lista=[]

while len(lista) < 10:
    num = int(input("Introduce un número (negativo para terminar): "))
    if num < 0:
        break
    lista.append(num)

print("Lista final:", lista)
