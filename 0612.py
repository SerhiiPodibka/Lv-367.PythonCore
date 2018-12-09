def newfunc(n):
    def myfunc(x):
        return x+name()
    return myfunc
newfunc(100)

def unknown (*args)

def func (a,b,c=2):
    return a+b+c

def func(a, b, p=9, r=8, *args **kwargs):
    return kwargs
#lambda functions
(lambda x:x**2)(3)
(lambda x,y:x+y)(1,2)

l=[1,2,3,4,5,6,7]
list(map(lambda x: x**3, l)) 

list1 = [7,2,3,10,12]
list2 = [-1,1,-5,4,6]
list(map(lambda x, y: x*y, list1, list2))

list(zip(list1,list2))
[x*y for x,y in zip(list1,list2) ]


numbers = [10,4,2,-1,6]
list (filter(lambda x: nonlocalx<5, numbers))

numbers = [2,3,4,5,6]
reduce (lambda res, x: res*x, numbers, 1)

def info()

def counter():
    num=0
    def incrementer():
        nonlocal num
        num+=1
        return numb
    return incrementer
c=counter()
print(c())
print(c())