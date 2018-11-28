fac = int(input('Введіть число для розрахунку факторіалу  '))
i = 1
factorial = 1
while i <= fac:
    factorial *= i
    i += 1
print("fac!",fac, "=", factorial)

a = int(input("Введіть значення змінної а "))
b = int(input("Введіть значення змінної b "))
if a > b:
    print ("Більше число", a)
elif a==b:
    print ("числа рівні")
else:
    print ("Більше число", b)

a = int (input("Введіть значення змінної а "))
if (a % 2) == 0:
        print ("Парне число")
else:
        print ("Непарне число")
