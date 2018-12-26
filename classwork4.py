def rectangle ():
    a = float(input("a= "))
    b = float(input("b= "))
    print("area=", a*b)
    
def trangle ():
    a = float(input("a= "))
    h = float(input("h= "))
    print("area=", 0.5*a*h)
def circle ():
    r = float(input("n= "))
    print("area=", 3.14*r**2)                                
            
figure = input ("1-rectangle, 2-trangle, 3-circle:")
if figure == "1":
    rectangle()
elif figure == "2":
    trangle()
elif figure =="3":
    circle()
else:
    print ("wrong")


def sum(x):
    i=0
    while x!=0:
        i=i+x%10
        x//10
    return i


def discriminant():
    a=float(input('enter a='))
    b=float(input('enter b='))
    c=float(input('enter c='))
    print(a,'x**2 +',b,'x +',c,'=0')
    print('D=b^2–4ac')
    return (b**2)+(4*a*c)



def multiply(a,b):
    return a*b
def summa(a,b):
    return a+b
def minus(a,b):
    return a-b
def divide(a,b):
    return a/b
def degree(a,b):
    return a**b
def root(a):
    return a**0.5
print(' add-1, minus-2, multiply-3, divide-4, degree-5, root-6, EXIT- 7')
i=1
while i==1:
    choice=input('choose an action:')
    if  choice=='1':
        print(a=float(input('enter number:')),'+', b=float(input('enter number:')))    
        print('=', summa(a,b))
    elif choice=='2':
        print(a=float(input('enter number:')),'-', b=float(input('enter number:')))    
        print('=', minus(a,b))
    elif choice=='3':
        print(a=float(input('enter number:')),'*', b=float(input('enter number:')))
        print('=', multiply(a,b))
    elif choice=='4':
        print(a=float(input('enter number:')),'/', b=float(input('enter number:')))
        print('=', divide(a,b))
    elif choice=='5':
        print(a=float(input('enter number:')),'**', b=float(input('enter number:')))
        print('=', degree_of_number(a,b))
    elif choice=='6':
        a=int(input('enter number:'))
        print('^0.5=', root(a))
    elif choice=='7':
        print('thanks that you used my app')
        break

        
  def fibonacci(a):
    m=0
    n=1
    s=0
    print('Числа фібоначі до числа ', a)
    while m<a:
        print (m)
        s=m+n
        n=m
        m=s
f=int(input("Введіть число  "))
fibonacci(f)
