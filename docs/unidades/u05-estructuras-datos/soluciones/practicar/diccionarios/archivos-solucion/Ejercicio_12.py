# Ejercicio 12
'''Usa un diccionario para almacenar los datos de varios estudiantes. 
Para cada uno guarda su nombre como clave y como valor otro diccionario
 con `'nota1'`, `'nota2'`, `'nota3'`. Crea al menos 3 estudiantes. 
 Luego, calcula la nota media de cada alumno.'''

estudiantes = {
    'Ana': {'nota1': 7, 'nota2': 8, 'nota3': 9},
    'Luis': {'nota1': 6, 'nota2': 7, 'nota3': 8},
    'Marta': {'nota1': 9, 'nota2': 8, 'nota3': 10}
}
for nombre, notas in estudiantes.items():
    media = sum(notas.values()) / len(notas)
    print(f"{nombre}: Nota media = {media:.2f}")
