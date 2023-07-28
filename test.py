import CalculateModule as cm
print(cm.abc)



a = cm.OddEven(10)
b= cm.PrimeNumber(11)

print(b)

print(a)

class Child(cm.Calculate):
    divied_number = 8

    def __init__(self, *num1):
        
        super().__init__(num1)
        self.new_list = sorted(set(num1))


    def percentage(self):
        print(f"Father Addition : {super().addition()}")
        total = sum(self.new_list) / len(self.new_list)
        print(self.divied_number)
        g_total = total / self.divied_number
        print(g_total)

        f_total =  super().addition() / len(self.list1)
        f_g_total = f_total / super().divied_number
        return   {"child": g_total, "father":f_g_total}
    
c=Child(10,20,30)

print(c)