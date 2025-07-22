print("Number to word Conersion:")
n = int(input("Enter a number: "))
digits = []
conversion = {1:"one",
              2:"Two",
              3:"Three",
              4:"Four",
              5:"Five",
              6:"Six",
              7:"Seven",
              8:"Eight",
              9:"Nine",
              10:"Ten"}
while n:
    digit = n%10
    digits.append(digit)
    n //=10
digits.reverse()
for i in digits:
    print(conversion[i],end=" ")