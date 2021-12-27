inp = input('Enter a number: ')
list = []
while inp != 'done':
    if not inp == 'done':
        try:
            list.append(float(inp))
        except:
            print('Please type number ')
            
    inp = input('Enter a number: ')

print(list)
print('Maximum: ',max(list))
print('Minimum: ',min(list))
