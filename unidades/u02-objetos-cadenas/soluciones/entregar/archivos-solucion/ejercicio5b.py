#  Fecha desde nombre de backup y cambiar extensión a .zip (find, [:]], replace)
nombre = "backup_2025_09_03.tar.gz"
print("Nombre de archivo: ", nombre)

pos1 = nombre.find("_")



pos2 = nombre.find("_", pos1+1)
pos3 = nombre.find("_", pos2+1)
pos4= nombre.find(".")

anio = nombre[pos1+1:pos2]
mes = nombre[pos2+1:pos3]
dia = nombre[pos3+1:pos4]

fecha = dia + "-" + mes + "-" + anio
print("Fecha: ", fecha)

nuevo = nombre.replace(".tar.gz", ".zip")
print("Nuevo nombre: ", nuevo)


#este nuevo nombre no se pide en el ejercicio
inicio_nombre = nombre[:pos1]
nuevo_nombre_fecha = inicio_nombre + "_" + fecha + ".zip"
print("Nuevo nombre con fecha cambiada: ", nuevo_nombre_fecha)
####