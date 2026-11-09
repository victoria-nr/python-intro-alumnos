# Username a partir de nombre y apellido (strip, replace, [:], random, string)
import random
import string

nombre = "  Ana  "
apellido = "  López "
print("Nombre y apellidos: ", nombre, " ", apellido)

nombre = nombre.strip()
apellido = apellido.strip()

usuario = nombre[:3]+apellido[:3]

usuario_limpio = usuario.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú','u')

d1 = random.choice(string.digits)
d2 = random.choice(string.digits)

username = usuario_limpio + d1 + d2
print("Nombre de usuario: ", username)
