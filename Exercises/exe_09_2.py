file = open('mbox-short.txt')

count = dict()

for line in file :
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2 :
            word = words[2]
            count[word] = count.get(word,0)+1
print(count)
