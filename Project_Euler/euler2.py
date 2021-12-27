def fib(to):
    a = 1
    b = 2
    sum = 0
    while a < to :
        if a%2 == 0:
            sum += a
        a ,b = b , a+b

    print(sum)
fib(4000000)
