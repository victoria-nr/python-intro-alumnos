#Partes de una ruta Windows (find, index, [:]])
ruta = "C:\\Users\\alumno\\Desktop\\proyecto"
print("Ruta: ", ruta)

pos1 = ruta.find("\\")
unidad = ruta[0]

resto1 = ruta[pos1 + 1:]
pos2_rel = resto1.find("\\") #hasta Users
resto2 = resto1[pos2_rel + 1:] #desde alumno

pos3_rel = resto2.find("\\") 
usuario = resto2[:pos3_rel]

resto3 = resto2[pos3_rel + 1:] # desde Desktop
pos4_rel = resto3.find("\\")
desktop = resto3[:pos4_rel]

print("Unidad: ", unidad)
print("Usuario: ", usuario)
print("Carpeta: ", desktop)
