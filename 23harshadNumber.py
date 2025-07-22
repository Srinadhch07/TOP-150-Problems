# A Harshad number, also known as a Niven number, is a positive integer that is divisible by the sum of its digits
n = int(input("Enter a number: "))
digits = []
while n:
    digit = n%10
    digits.insert(0,digit)
    n //=10
print("Harshad Number " if  n%sum(digits)==0 else "Not an Harshad Number")
