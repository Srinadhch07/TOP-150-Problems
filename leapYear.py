# (year%4==0)AND(year%100==0)OR(year%400==0)
value = int(input("Enter year: "))
print("Leap Year" if (value%4 == 0) and (value%100 !=0) or (value%400 == 0) else "Not a Leap year")