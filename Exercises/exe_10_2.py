file = open('mbox-short.txt')
list = list()
dict = dict()
for line in file :
    if line.startswith('From'):
        word = line.split()
        if len(word) > 4:
            hour = word[5].split(':')[0]
            dict[hour]= dict.get(hour,0)+1
dict = sorted(dict.items())
for i in dict :
    print(i[0],i[1])
