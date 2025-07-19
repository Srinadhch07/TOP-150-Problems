def primerange(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

input  = int(input("Enter range: "))

for i in range(1,input):
    if primerange(i):
        print(i, end=" ")


