table = int(input("Enter table number: "))
for i in range(1,11):
    print(f'{table} * {i} = {table*i}')
    
print("\n".join([f'{table} * {i} = {table*i}' for i in range(1,11)]))