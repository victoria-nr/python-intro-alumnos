#  Fecha desde nombre de backup y cambiar extensión a .zip (find, [:]], replace)
nombre = "backup_2025_09_03.tar.gz"
print("Nombre de archivo: ", nombre)

pos1 = nombre.find("_")
resto1 = nombre[pos1 + 1:]


pos2_rel = resto1.find("_")
anio = resto1[:pos2_rel]

resto2 = resto1[pos2_rel + 1:]
pos3_rel = resto2.find("_")
mes = resto2[:pos3_rel]

resto3 = resto2[pos3_rel + 1:]
pos4_rel = resto3.find(".")
dia = resto3[:pos4_rel]

fecha = dia + "-" + mes + "-" + anio
print("Fecha: ", fecha)

nuevo = nombre.replace(".tar.gz", ".zip")
print("Nuevo nombre: ", nuevo)


#este nuevo nombre no se pide en el ejercicio
inicio_nombre = nombre[:pos1]
nuevo_nombre_fecha = inicio_nombre + "_" + fecha + ".zip"
print("Nuevo nombre con fecha cambiada: ", nuevo_nombre_fecha)
####