a = map(int,input("Enter elements: ").split())
even = []
odd = []
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Count of\nEven :{len(even)}\nOdd :{len(odd)}")