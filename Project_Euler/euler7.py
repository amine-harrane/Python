#def is_prime(n):
#    for i in range(2,n):
#            if n % i == 0 :
#                return
#            else :
#                continue
#    return n
#
#i = 2
#count = 0
#while count != 10001:
#    t = is_prime(i)
#
#    if t != None :
#        count += 1
#        print(count,t)
#    i += 1


import math

def n_th_prime(n):

    prime_count = 0
    array_count = 100

    while array_count // math.log(array_count) < n * 3 :
        array_count *= 2

    is_prime_array = [True] * array_count
    for i in range (2,array_count):
        k = i + i
        if is_prime_array[i] :
            while k < array_count :
                is_prime_array[k] = False
                k += i
            prime_count += 1
            if prime_count == n :
                return is_prime_array[:i+1]

print(len(primes_bellow_two_million(6))-1)
