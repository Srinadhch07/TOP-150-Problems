class fib:
    def __init__(self,n):
        print("Fibonacci series: ",end = " ")
        a = self.fib #Assigning method object to 'a'
        a(n) # Calling method using it's object
    def fib(self,n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a,b=0,1
            print(a,b,end=" ")
            for _ in range(2,n+1):
                c = a+b
                a = b
                b = c
                print(c,end=" ")
            return None
n = int(input("Enter a number: "))
fibObj = fib(n)