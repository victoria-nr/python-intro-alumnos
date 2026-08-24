# Enunciado: Por sys.argv recibe un fichero y muestra líneas, palabras y caracteres. Error si no existe.

import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Uso: python ejer10.py <fichero.txt>")
else:
    ruta = Path(sys.argv[1])

    if not ruta.exists():
        print("El fichero no existe:", ruta)
    else:
        texto = ruta.read_text(encoding="utf-8")
        num_lineas = len(texto.splitlines())
        num_palabras = len(texto.split())
        num_caracteres = len(texto)

        print("Fichero:", ruta)
        print("Líneas:", num_lineas)
        print("Palabras:", num_palabras)
        print("Caracteres:", num_caracteres)

