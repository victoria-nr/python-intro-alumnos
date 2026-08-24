#factorial
res = 1

num = int(input("Dime un número: "))

for contador in range(2, num + 1):
    res *= contador

print(f"El resultado es {res}")
