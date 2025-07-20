# A strong number, also known as a Krishnamurthy number or Factorion, is a number in which the sum of the factorials of its individual digits is equal to the number itself. 
n = int(input("Enter a number: "))
digits = []
while n > 0:
    digits.append(n%10)
    n //=10
def factorial(d):
    return 1 if d == 0 or d == 1 else  d * factorial(d-1)
print(sum([factorial(d) for d in digits]))

