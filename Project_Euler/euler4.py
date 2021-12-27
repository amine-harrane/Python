def pal():
    max = 0
    for i in range(100,1000):
        for j in range(100,1000):
            x = i * j
            if x / 100000 > 1 :
                y = str(x)
                if y[0]==y[5] and y[1] == y[4] and y[2] == y[3]  :
                    if max < x :
                        max = x
    print(max)
pal()
