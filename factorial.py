class factorial:
    def __init__(self):
        n = int(input('Enter a value:'))
        value = 1
        for i in range(1,n+1):
            value *= i
        print("Factorial number :",value)

factorialObj = factorial()