
def arithmetic_arranger(arranger,answer=False):
    nums1=[]
    operators_nums2=[]
    dash = []
    sums=[]
    if len(arranger) > 5:
        return 'Error: Too many problems.'

    for problem in arranger :
        num1 = problem.split()[0]
        num2 = problem.split()[2]
        operator = problem.split()[1]


        if operator != '+' and operator != '-':
             return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit() :
             return "Error: Numbers must only contain digits."
        if int(num1) // (10**4)>0 or int(num2) // (10**4)>0 :
             return "Error: Numbers cannot be more than four digits."
        if operator == '+':
             sum=int(num1) + int(num2)
        else:
             sum=int(num1) - int(num2)
        if len(num1)> len(num2):
             num1 = num1.rjust(len(num1)+2)
             num2 = num2.rjust(len(num1)-1)
        else:
             num1 = num1.rjust(len(num2)+2)
             num2 = num2.rjust(len(num2)+1)
        sum = str(sum).rjust(len(num1))
        nums1.append(num1)
        operators_nums2.append(operator+num2)
        dash.append('-'*len(num1))
        sums.append(sum)

    nums1= '    '.join(nums1)
    operators_nums2 = '    '.join(operators_nums2)
    dashs = '    '.join(dash)
    sums = '    '.join(sums)
    if answer == True :
        return nums1 +"\n" +operators_nums2+'\n' +dashs+'\n' +sums
    else:
        return nums1+'\n' +operators_nums2+'\n'+ dashs
