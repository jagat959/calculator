num = (input('Enter a number = '))
num2 = int(input('Enter a number = '))
operator = input('Enter the operator: ')


#typeconversion
num = int(num)
result=''
if operator == '+':
    result = num+num2
elif operator =='*':
    result = num*num2
elif operator =='-':
    result = num-num2
elif operator =='/':
    result = num/num2
else:
    result='not defined'
print(result)