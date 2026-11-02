# Partes de un email institucional (index, find, [:]])
email = "admin.redes@centro.edu"
print("Email: ", email)

pos_arroba = email.index("@")
usuario = email[:pos_arroba]
print("Usuario: ", usuario)

resto = email[pos_arroba + 1:]
pos_punto = resto.find(".")
dominio = resto[:pos_punto]
print("Dominio: ", dominio)

tld = resto[pos_punto + 1:]
print("Tld: ", tld)

