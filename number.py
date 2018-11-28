n = str(input ("Введіть 4-х значне число "))
a = len(n)
if  a == 4:
    print (int (n[0]) * int (n[1]) * int (n [2]) * int (n[3]))
    print (int (n [::-1]))
    print (int(''.join(sorted(n))))

else:
    print ('Ви ввели не 4-ч значне число')
