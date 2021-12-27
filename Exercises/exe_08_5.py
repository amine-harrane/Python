
file = input ('Enter a file name: ')
txt = open('mbox-short.txt')

count =0
for line in txt :
    if line.startswith('From'):
        print(line.split()[1])
        count += 1
print('There were ',count, 'lines in the file with From as the Firs word')
