#Pistas: librería platform 
#Detecta e imprime el sistema operativo, la versión y el procesador del equipo
#  en donde se ejecuta el script. A continuación, muestra el gestor de paquetes 
# recomendado según las siguientes indicaciones: 
#- Windows -> "winget" 
#- Linux -> "apt" 
#- macOS (Darwin) -> "brew" 
#Para otros sistemas, muestra "gestor no definido". 
import platform

so = platform.system()
print("SO:", so)
print("Versión: ", platform.release())
print("Procesador: ", platform.processor())


if so == "Windows":
    print("Gestor recomendado: winget")
elif so == "Linux":
    print("Gestor recomendado: apt")
elif so == "Darwin":
    print("Gestor recomendado: brew")
else:
    print("Gestor no definido")
