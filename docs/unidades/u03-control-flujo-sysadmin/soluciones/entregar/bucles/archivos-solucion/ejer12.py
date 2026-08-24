# Ejer12 - Validar contraseña simple con bucles (while + for sobre cadena)
# Enunciado:
# Pide una contraseña hasta que cumpla:
# - Al menos 6 caracteres
# - Contiene al menos un dígito
# Usa while para repetir y un for para comprobar si algún carácter es dígito.
while True:
    pwd = input("Contraseña: ")
    tiene_digito = False

    for ch in pwd:
        if ch.isdigit():
            tiene_digito = True

    if len(pwd) >= 6 and tiene_digito:
        print("OK")
        break
    else:
        print("No válida. Intenta de nuevo.")
