# 1: if  n <=1 return false
# 2: Find the max limit for checking prime or not using sqrt(n)
# 3: IF: any number till the max limit returns quotient zero it is not prime number
#     ELSE: it is prime number 
import math
class PrimeNumber:
    def prime(self,n):
        if n <= 1: return False
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0: return False
        return True
primeObj = PrimeNumber()
n = int(input("Enter a number: "))
print("Prime number:", primeObj.prime(n))