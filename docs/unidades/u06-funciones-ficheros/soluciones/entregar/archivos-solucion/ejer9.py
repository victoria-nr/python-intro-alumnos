# Enunciado: Crea cleanup_plan.txt y genera cleanup_report.txt con existencia y recuento de elementos.

from pathlib import Path

carpetas = ["/tmp", "/var/tmp", "/noexiste"]

Path("cleanup_plan.txt").write_text("\n".join(carpetas) + "\n", encoding="utf-8")

salida = []

with open("cleanup_plan.txt", "r", encoding="utf-8") as f:
    for linea in f:
        ruta = Path(linea.strip())

        if ruta.exists() and ruta.is_dir():
            cantidad = 0
            for elem in ruta.iterdir():
                cantidad+=1
                
            salida.append(f"{ruta} -> existe -> elementos: {cantidad}")     
                
        else:
            salida.append(f"{ruta} -> NO existe")

with open("cleanup_report.txt", "w", encoding="utf-8") as f:
    for linea in salida:
        f.write(linea + "\n")

#Alternativa        
#Path("cleanup_report.txt").write_text("\n".join(salida) + "\n", encoding="utf-8")
print("Generado cleanup_report.txt")

