print("""
********************************************************
                    Nested Class 
********************************************************
""")



class army:                         # Outer Class 

    def __init__(self):             
        self.name = "Karan"
        self.gn = self.Gun()          # Call Nested Class 


    def show(self):
        print(f"Name : {self.name}")


    
    class Gun:                          # Inner class 

        def __init__(self):
            self.name = "M4"
            self.capacity = "40 Round"
            self.range = "Long Range"


        def disp(self):
            print(f"Gun Name : {self.name}")
            print(f"Gun capacity : {self.capacity}")
            print(f"Gun range : {self.range}")



            
        