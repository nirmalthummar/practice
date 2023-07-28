from CalculateModule import Calculate , OddEven, abc, PrimeNumber as pm




print(abc)



a = OddEven(7)
print(a)




class Child(Calculate):
    divied_number = 8

    def __init__(self, *num1):
        
        super().__init__(num1)
        self.new_list = sorted(set(num1))


    def percentage(self):
        print(f"Father Addition : {super().addition()}")
        total = sum(self.new_list) / len(self.new_list)
        g_total = total / self.divied_number


        f_total =  super().addition() / len(self.list1)
        f_g_total = f_total / super().divied_number
        return   {"child": g_total, "father":f_g_total}