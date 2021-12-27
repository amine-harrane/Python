
file = open('mbox-short.txt')
dict = dict()
list = list()
def Read_parse(file):
    for line in file :
        if line.startswith('From'):
            email = line.split()[1]
            dict[email]= dict.get(email,0) +1


Read_parse(file)
for email,count in dict.items():
    email_count = (count,email)
    list.append(email_count)
list = sorted(list , reverse = True)
print(list[0][1] , list[0][0] )
