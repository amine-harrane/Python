file = input('Enter file: ')
try:
    romeo = open(file)
except:
    print('no file , try again')
    quit()

list = []
for line in romeo :
    for i in line.split()  :
        if i in list :
            continue
        list.append(i)

list.sort()
print(list)
