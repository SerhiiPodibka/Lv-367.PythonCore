print ('Парні числа')
i=0
while i<100:
    if i%2 ==0:
        print (i)
    i=i+1
print ('Парні числа') 
for i in range(100):
    if i%2 ==0:
        print (i)
print ('Непарні числа')
for item in range(100):
        if not item % 2 > 0:
            continue
        print (item)
print ('Непарні числа')
for i in range(100):
    if i%2 >0:
        print (i)


test_list = [2, 4, 6, 8, 9, 10]
contains_odd = False
for item in test_list:
    if not item % 2 == 0:
        contains_odd = True
        break
if contain_odd:
    print ("There are odd numbers")
else:
    print ("There are only event numbers")

list_number = [1,2,3,4]
print (list_number)
i=0
for a in list_number: 
    list_number[i] = float(a)
    i=i+1
print (list_number)

f1 = 0 
f2 = 1
n=7 
i = 0 
while i < n:
    f_sum = f1 + f2 
    print(f_sum)
    f2 = f_sum
    f1 = f2
    i = i + 1
    
list = ['a', 'b', 'c', 'd']
i = 0
for i in list:
    print (i)

list = ['a', 'b', 'c', 'd']
for i in list:
    print (i, end ="#")
    
