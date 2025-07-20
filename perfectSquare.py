# if Sum of proper divisors excluding itself is equal to number, then it called perfect number
n = int(input("Enter a number: "))
divisors = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        divisors.append(i)
        divisors.append(n//i)
divisors.sort()
divisors.pop()
print("perfect Number" if sum(divisors) == n else "Not a perfect number")

