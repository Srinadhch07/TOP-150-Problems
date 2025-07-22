n = int(input("Enter number : "))
digits = []
while n:
    digit = n%10
    digits.append(digit)
    n //=10
print(f"First number {digits[-1]}\nLast number {digits[0]}")
