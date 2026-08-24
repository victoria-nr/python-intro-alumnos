# Enunciado: Pide al usuario una palabra y guárdala en `palabras.txt` sin borrar el contenido anterior.

palabra = input("Introduce una palabra: ")

with open("palabras.txt", "a", encoding="utf-8") as f:
    f.write(palabra + "\n")

print(f"Guardado en palabras.txt la palabra: {palabra}")
