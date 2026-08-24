
notas = []

for i in range(5):
    nota=-1.0
    while nota < 0 or nota > 10:
        nota = float(input(f"Introduce la nota {i + 1} (entre 0 y 10): "))
      
    notas.append(nota)


print("\nLas notas ingresadas son:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")


nota_media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"\nNota media: {nota_media:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
