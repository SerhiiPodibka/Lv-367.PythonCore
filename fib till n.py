fib1 = 0 
fib2 = 1
n = 3 # число до якого буде виконуватись цикл
i = 0 # лічильник циклу
while i < n:
    fib_sum = fib1 + fib2 # тимчасова змінна, яка є суммою 2-ч чисел
    print(fib_sum)
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1