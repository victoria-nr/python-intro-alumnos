#Partes de una ruta Windows (find, index, [:]])
ruta = "C:\\Users\\alumno\\Desktop\\proyecto"
print("Ruta: ", ruta)

unidad = ruta[0]

pos1 = ruta.find("\\")

pos2 = ruta.find("\\", pos1+1)

pos3 = ruta.find("\\", pos2+1)

pos4 = ruta.find("\\", pos3+1)

usuario= ruta[pos2+1:pos3]
carpeta = ruta[pos3+1:pos4]

print("Unidad: ", unidad)
print("Usuario: ", usuario)
print("Carpeta: ", carpeta)