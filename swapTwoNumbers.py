a,b = map(int,input("Enter numbers: ").split())
# 2,3
class swapNumbers:
    def with_temp(self,a,b):
        temp = a
        a = b
        b = temp
        print(f"a={a},b={b}.")
    def without_temp(self,a,b):
        a,b = a+b,a
        a,b = a-b,b
        print(f"a={a},b={b}.")
swapObj = swapNumbers()
swapObj.with_temp(a,b)
swapObj.without_temp(a,b)
