n = int(input("Enter a number: "))
digits = []
while n:
    digit = n%10
    digits.append(digit)
    n = n//10
product = 1
for i in digits:
    product *= i
print("Product of Digits: ",product)