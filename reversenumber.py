n = int(input('Enter a number: '))
reversed_num = 0
while n > 0:
    digit = n%10 # last digit
    reversed_num = reversed_num * 10 + digit 
    n = n//10 # removing last digit
print(reversed_num)