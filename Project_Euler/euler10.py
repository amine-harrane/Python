#def primes_below(to):
#    i = 2
#    count = 0
#    sum = 17
#    while i < to :
#        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 :
#            i += 1
#            continue
#        for n in range(1,i):
#            if i % n == 0 :
#                count = 0
#                continue
#            else :
#                count += 1
#        if count == n-1 :
#            sum = sum + i
#            print(i)
#        i+=1
#    print(sum)
#primes_below(2000000)


array_count = 2000000
primes_array = [True]* array_count
sum = 0

def   summation_of_primes(array_count):

    for i in range(2,len(array_count)):
        k = i+i
        if primes_array[i]:
            while k < len(array_count):
                primes_array[k]=False
                k += i

summation_of_primes(primes_array)
for j in range(2,array_count):
        if primes_array[j]:
            #print(len(primes_array[:j]),sum)
            sum += j
print(sum)
