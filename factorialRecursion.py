class Factorial:
    def factorial(self,n):
        if n == 1 or n== 0:
            return 1
        else:
            return n*self.factorial(n-1)
input = int(input("Enter number: "))
factorialObj = Factorial()
value = factorialObj.factorial(input)
print("Factorial : ",value)