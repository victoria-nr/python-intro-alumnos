import random
lista=[]
for _ in range(10):
    numero =random.randint(1, 100)
    lista.append(numero)

print("Lista original:", lista)

lista.sort()

print("Lista ordenada:", lista)
