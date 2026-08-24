
temp_min = []
temp_max = []
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

for i in range(7):
    print(f"\nDía {dias[i]}:")
    mint = float(input("Introduce la temperatura mínima: "))
    maxt = float(input("Introduce la temperatura máxima: "))

    temp_min.append(mint)
    temp_max.append(maxt)

print("\nTemperatura media de cada día:")
for i in range(7):
    media = (temp_min[i] + temp_max[i]) / 2
    print(f"Día {dias[i]}: {media:.2f}°C")


min_t = min(temp_min)
print("\nDías con menor temperatura mínima:")
for i in range(7):
    if temp_min[i] == min_t:
        print(f"Día {dias[i]}: {temp_min[i]}°C")


temp = float(input("\nIntroduce una temperatura máxima para buscar: "))
existe = False
for i in range(7):
    if temp_max[i] == temp:
        print(dias[i])
        existe=True
if not existe:
    print("No hay días con esa temperatura máxima.")
