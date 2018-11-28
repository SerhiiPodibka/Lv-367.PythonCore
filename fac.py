fac = int(input('Введіть число для розрахунку факторіалу  '))
i = 1
factorial = 1
while i <= fac:
    factorial *= i
    i += 1
print("fac!",fac, "=", factorial)
