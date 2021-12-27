def smallest(n):
    count = 0
    while True :
        for i in range(1,21):
            if n % i == 0 :
                count += 1
                if count == 20 :
                    return n
                continue
            elif n % i != 0:
                count = 0



        break
n=1
while True :
    if smallest(n) is not None :
        print(smallest(n))
        break
    n+=1
