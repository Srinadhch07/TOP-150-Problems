# The Greatest Common Divisor (GCD) of two numbers is the largest positive integer that divides both numbers without leaving a remainder
# If b is not zero, then:
# GCD(a, b) = GCD(b, a % b)
a,b = map(int,input("Enter two numbers: ").split())
while b:
    a,b = b, a%b
print(a)