file = open('mbox-short.txt')
count = dict()

for line in file :
    if line.startswith('From'):

        email = line.split()[1]

        count[email]= count.get(email,0) +1


count_domain = dict()
for email in count :
    domain_name = email.split('@')[1]
    count_domain[domain_name]= count_domain.get(domain_name , 0) +1
print(count_domain)
