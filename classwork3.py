nums = [] #створюємо порожній список
k=int(input("введіть кількість елементів")) #вводимо кількість елементів списку
for i in range(k):
    n=int(input("enter the element"))
    nums.append(n) #обєднуємо елементи списку
print (nums)
max = nums[0]
min = nums[0]
for i in range(k):
    if nums[i]>max:
        max=nums[i]

    if nums[i]<min:
        min=nums[i]
print ("max number = %d.min number = %d."%(max,min))

for x in range (1,11):
    if x%2 ==0:
        print (x,"is even na 2")
    elif x%3 ==0:
        print (x,"is even na 3")
    else:
        print (x,"is na 2 and na 3")


while True:
    a = int(input('chuslo'))
    if a<=0:
        break

k=int(input("введіть кількість елементів"))
for i in range(k):
    n=int(input("enter the element"))
    if n<=0:
        break

login="First"
a=input("Введіть логін ")
if a==login:
    print("Welcome!")
while a!=login:
    print('error')
    break
    
i=0
while i==0:
    a=int(input("enter number "))
    if a<=0:
        print ("your number is negative or 0")
        i+=1
