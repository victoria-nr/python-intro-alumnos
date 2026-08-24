# Ejercicio 10: 


paquetes = ["vim", "curl", "htop"]

nuevo = input("Introduce otro paquete que quieras instalar: ")
paquetes.append(nuevo)

comando = "apt install " + " ".join(paquetes)

print("\nComando generado:")
print(comando)
