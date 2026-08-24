# Ejercicio 7
'''Escribe un programa que cuente cuántas veces aparece cada letra 
en una palabra introducida por el usuario. Usa un diccionario para
 almacenar el resultado. Ejemplo: en la palabra 'amiga' la 'a' 
 aparece 2 veces, la 'm' 1 vez, la 'i' 1 vez y la 'g' 1 vez.'''

palabra = input("Introduce una palabra: ")
conteo = {}

for letra in palabra:
    if letra not in conteo:
        conteo[letra]=1
    else:
        conteo[letra]+=1
print(conteo)

#forma más compacta
#for letra in palabra:
#    conteo[letra] = conteo.get(letra, 0) + 1
#print(conteo)


