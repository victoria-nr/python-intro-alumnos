# Ejercicio 11
'''Dado un texto introducido por teclado, muestra cuántas veces aparece
 cada vocal usando un diccionario. Usa una sola pasada sobre el texto.'''

texto = input("Introduce un texto: ")
vocales = 'aeiou'
conteo = {v: 0 for v in vocales}
for letra in texto.lower():
    if letra in conteo:
        conteo[letra] += 1
print(conteo)
