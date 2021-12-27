def list_factor(to):
    j = 0
    for i in range(2,to):
        if to % i == 0 :
            j = to
            break
        else :
            continue
    if j !=to :
        j = to
        return j
num = 600851475143
for i in range(1,num):
    if list_factor(i) is None :
        continue
    elif num % list_factor(i) == 0 :
        print(list_factor(i))
