print("Reversing a number using Recursion")
reversed_num = 0
def reverse(n):
    global reversed_num
    if n<=0:
        return reversed_num
    digit = n%10
    reversed_num = reversed_num*10 + digit
    n //=10
    return reverse(n)
n = int(input("Enter a number :"))
print("Reversed Number: ",reverse(n))

