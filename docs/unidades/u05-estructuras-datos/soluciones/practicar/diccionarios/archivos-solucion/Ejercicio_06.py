# Ejercicio 6
'''Dado el siguiente diccionario:

puntuaciones = {'Juan': 85, 'Ana': 92, 'Luis': 78}

Actualiza la puntuación de `'Luis'` a 88. Luego elimina a `'Juan'` del diccionario y muestra el resultado final.'''

puntuaciones = {'Juan': 85, 'Ana': 92, 'Luis': 78}
puntuaciones['Luis'] = 88
del puntuaciones['Juan']
print(puntuaciones)
