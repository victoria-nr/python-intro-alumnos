# Enunciado: En `configs/` (con subcarpetas), busca `*.conf` con `rglob()` y guarda en `conf_list.txt` su ruta relativa.
from pathlib import Path

base = Path("configs")

if not base.exists():
    print("No existe la carpeta 'configs'. Créala con subcarpetas y ficheros .conf para probar.")
else:
    rutas_relativas = []
    for fichero in base.rglob("*.conf"):
        rutas_relativas.append(str(fichero.relative_to(base)))

    Path("conf_list.txt").write_text("\n".join(rutas_relativas) + ("\n" if rutas_relativas else ""), encoding="utf-8")
    print("Generado conf_list.txt con", len(rutas_relativas), "ficheros .conf")
