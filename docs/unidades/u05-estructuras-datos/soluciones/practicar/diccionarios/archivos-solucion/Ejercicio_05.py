# Ejercicio 5
'''Crea un diccionario vacío. Luego, pide al usuario que introduzca 
por teclado 3 pares clave-valor para rellenarlo. 
Finalmente, imprime el diccionario.'''
mi_dic = {}
for _ in range(3):
    clave = input("Introduce una clave: ")
    valor = input("Introduce un valor: ")
    mi_dic[clave] = valor
print(mi_dic)
