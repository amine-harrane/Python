# def arithmetic_arranger(list,answer=False):
#     operator = None
#     line1 = []
#     line2 = []
#     line3 = []
#     if len(list) > 5 :
#         return "Error: Too many problems"
#     for problem in list :
#         digit = problem.split()
#         num1 = digit[0]
#         operator = digit[1] + ' '
#         num2 = digit[2]
#         line1.append(num1.rjust(5)+'    ')
#         line2.append(operator+num2.rjust(3)+'    ')
#         dash = '-' * max(len(num1),len(num2)) + (2*'-')+'    '
#         line3.append(dash)
#     if operator != '+ ' and operator!='- ':
#         return "Error Operator must be '+' or '-'."
#     try:
#         num1=int(num1)
#         num2=int(num2)
#     except:
#         return 'Error: Numbers must only contain digits.'
#
#     if num1 // (10**3) > 1:
#         return 'Error: Numbers cannot be more than four digits.'
#     if answer==True:
#         return num1 + num2
#     print(''.join(line1))
#     print(''.join(line2))
#     return ''.join(line3)
#
# list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# print(arithmetic_arranger(list))

def arithmetic_arranger(list,answer=False):
    if len(list)>5 :
        return "Error: Too many problems."
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    dash=''
    for problem in list :
        num1 = problem.split()[0]
        num2 = problem.split()[2]
        operator = problem.split()[1]
        try:
            if operator == '+':
                sum1_2 = int(num1)+int(num2)
            else:
                sum1_2 = int(num1)-int(num2)
        except:
            return "Error: Numbers must only contain digits."
        if operator != '+' and operator != '-':
             return "Error: Operator must be '+' or '-'."

        if int(num1) // (10**4) > 0 or int(num2) // (10**4)>0 :
             return "Error: Numbers cannot be more than four digits."
        if len(num1)>len(num2):
            num1=num1.rjust(len(num1)+2)
            num2=num2.rjust(len(num1)-1)
            sum1_2=str(sum1_2).rjust(len(num1))
            dash='-'*(len(num1))
        else:
            num1=num1.rjust(len(num2)+2)
            num2=num2.rjust(len(num2)+1)
            sum1_2=str(sum1_2).rjust(len(num2)+1)
            dash='-'*(len(num2)+1)
        line1.append(num1)
        line2.append((operator+num2))
        line3.append(dash)
        line4.append(sum1_2)
    line1 = '    '.join(line1)
    line2 = '    '.join(line2)
    line3 = '    '.join(line3)
    line4 = '    '.join(line4)
    arranged_problems = line1+ '\n' + line2+ '\n' + line3
    if answer == True :
        arranged_problems += '\n'+line4
    return arranged_problems







arguments = []
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
