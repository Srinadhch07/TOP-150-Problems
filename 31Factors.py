n = int(input("Enter a number :"))
factors = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        factors.append(i)
        factors.append(n//i)
factors = set(factors)
factors = sorted(list(factors))
print(f"Factors: {factors}")
