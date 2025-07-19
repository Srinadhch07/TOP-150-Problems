# Finding power of a number
# def pow(a,b):
#     value = 1
#     for _ in range(b):
#         value *= a
#     print(value)
# a,b = map(int,input("Enter numbers: ").split())
# pow(a,b)

a,b = map(int,input("Enter values: ").split())
value = 1; 
[value := value *  a for _ in range(b)]
print(value)