# Password con patrón simple (string, random)
import string
import random

letras = string.ascii_letters
digitos = string.digits
simbolos = "!#$%&*"

a = random.choice(letras)
b = random.choice(letras)
c = random.choice(letras)
d = random.choice(letras)

e = random.choice(digitos)
f = random.choice(digitos)
g = random.choice(digitos)
h = random.choice(digitos)

i = random.choice(simbolos)
j = random.choice(simbolos)

password = a + b + c + d + e + f + g + h + i + j
print("Password generada: ", password)
