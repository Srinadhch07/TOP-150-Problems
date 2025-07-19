# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. 
input = int(input('Enter a number: '))
value = sum(int(d)**len(str(input)) for d in str(input))
print("Armstrong" if value == input else "Not armstrong")