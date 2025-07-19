# First Find the GCD then divide the product of numbers with GCD = LCM
# AxB/gcd
a,b = map(int, input("Enter numbers: ").split())
product = a*b
while b:
    a,b = b, a%b
# For LCM
LCM = product//a
print(LCM)