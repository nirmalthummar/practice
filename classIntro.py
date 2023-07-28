print("""
**************************************
            Class
**************************************
""")


class Calculate:
    a=40
    def __init__(self,*number):
        self.evenList = [i for i in number if i % 2 == 0]
        # print(self.evenList)
        self.add = self.addition()
        self.b=self.a
        print(self.b)
        
    def addition(self):
        count = 0
        print(f"Addition Method")
        for i in self.evenList:
            count += i
        return count


Cal = Calculate(1,2,3,4,5,6,7,8,9,0,0)

a = Cal.addition()

print(f"Method called : {a}")
print(f"attribute  : {Cal.evenList}")
# print(f"Method called in init  : {Cal.add}")










