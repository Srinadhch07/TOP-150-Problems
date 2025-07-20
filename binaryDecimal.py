class Decimal:
    def __init__(self,bin_value):
        self.decimal(bin_value)
        self.decimal_code(bin_value)
    def decimal(self,bin_value):
        print(int(bin_value,2))
    def decimal_code(self,bin_value):
       decimal = sum(int(bit) * 2**i for i,bit in enumerate(reversed(bin_value)))
       print(decimal)
decimalObj = Decimal(str(10111))




            