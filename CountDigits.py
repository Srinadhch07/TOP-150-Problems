n = int(input("Enter number: "))
counter = 0
while n > 0:
    counter +=1 # count
    n = n //10 # remove digit
print("Number of Digits: ",counter)
