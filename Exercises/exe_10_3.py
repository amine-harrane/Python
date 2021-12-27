
file = open("mbox-short.txt")
dict = dict()
list = list()
for line in file :
    line=line.lower()
    for i in range (len(line)):
        if line[i].islower():
            dict[line[i]]= dict.get(line[i],0)+1
    #for letter in line.split(""):
        #dict[letter]= dict.get(letter,0)+1
#print (dict)

list = [(v,k) for k,v in dict.items()]
print(list)
