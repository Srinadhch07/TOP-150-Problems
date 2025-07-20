# | Step | Divide By 2 | Quotient | Remainder |
# | ---- | ----------- | -------- | --------- |
# | 1    | 23 ÷ 2      | 11       | 1         |
# | 2    | 11 ÷ 2      | 5        | 1         |
# | 3    | 5 ÷ 2       | 2        | 1         |
# | 4    | 2 ÷ 2       | 1        | 0         |
# | 5    | 1 ÷ 2       | 0        | 1         |


class Bin:
    def bin(self,value):
        bin_value = bin(value)
        print("Binary value: ",bin_value)
    def bin_code(self,value):
        bin_values = []
        q = value
        while q > 0:
            q = value//2
            r = value % 2
            bin_values.append(r)
            value = q
        print("Binary values: ",''.join(map(str,bin_values[::-1])))
        
binObj = Bin()
value = int(input("ENter value: "))
binObj.bin(value)
binObj.bin_code(value)