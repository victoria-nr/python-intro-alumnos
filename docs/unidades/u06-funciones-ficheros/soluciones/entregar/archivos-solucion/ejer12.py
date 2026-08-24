# Enunciado: Lee system_report.txt y lo añade a system_report_history.txt separando con guiones.

from pathlib import Path

informe = Path("system_report.txt")

if not informe.exists():
    print("No existe system_report.txt. Ejecuta antes el ejercicio 1.")
else:
    contenido = informe.read_text(encoding="utf-8")

    with open("system_report_history.txt", "a", encoding="utf-8") as f:
        f.write(contenido)
        f.write("\n" + "-" * 30 + "\n")

    print("Añadido informe a system_report_history.txt")

