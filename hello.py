#print("menu:")
#print("1.Dosa")
#print("2.Idly")
#alue = int(input("Menu:\n1.Dosa\n2.Idly\nChoose your item: "))

a = 10
b = 2.0
c= '10'
d = "srinadh \nhello"
print(d)
e ="""srinadh 
chintak indi"""

f = True

g = [1,"2",3.0,True,1]
g.append(3)
h =(1,2,3,4,5,6,7,8,9,10,1)
i = {1,"srinadh",2,3,1}
j = {1:"srinadh",2:"madhan"}
k= {"srinadh":9346070083,"madhan":8688296682}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(h))

print(g)
print(h)
print(i)
print(j[2])
print(k["srinadh"])

print("---------------")

print(1)
print(2)
print(3)
print("---------------")

for i in range(1,11):
	print("* "*10)
print("---------------")
for i in reversed(range(1,11)):
	print("*"*i)
print("---------------")
for i in reversed(range(1,11)):
	print("* "*20)
print("---------------")
for i in range(1,6):
	for j in range(1,6):
		if i==1 or j==1 or j==5 or i ==5:
			print("*",end=" ")
		else:
			print(" ", end=" ")
		
	print("\n")





