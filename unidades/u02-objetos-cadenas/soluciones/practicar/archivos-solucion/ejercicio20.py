# Solicitar un carácter
caracter = input("Escribe un carácter: ")

# Mostrar su valor Unicode
print("Valor Unicode del carácter: ", ord(caracter))

# Solicitar valor entre 32 y 126
unicode_valor = int(input("Escribe un valor entre 32 y 126: "))

print("Carácter correspondiente: ", chr(unicode_valor))
