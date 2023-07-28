#### TASK 1 #####

### # METHOD 1 #####

def words_with_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    result = [word for word in words if any(vowel in word.lower() for vowel in vowels)]
    return result

# Test case
sentence = 'You have no rhythm'
result = words_with_vowels(sentence)
print(result)  # Output: ['You', 'have', 'no']


##### ## # METHOD 2 ########

def words_with_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    result = []
    for word in words:
        if any(vowel in word.lower() for vowel in vowels):
            result.append(word)
    return result

sentence = 'You have no rhythm'
result = words_with_vowels(sentence)
print(result)



#### ### ## TASK 2 ### ###### ###

class Car:
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    @classmethod
    def print_cars(cls, car_objects):
        for car in car_objects:
            print(f"car_model = {car.model}")
            print(f"Color = {car.color}")
            print(f"Year = {car.year}")
            print(f"Transmission = {car.transmission}")
            print(f"Electric = {car.electric}")
            print()

class Ford(Car):
    pass

# class BMW(Car):
#     pass

# class Tesla(Car):
#     pass

# Create car objects
# bmw1 = BMW("x6", "silver", 2018, "Auto", False)
# tesla1 = Tesla("S", "beige", 2017, "Auto", True)
ford1 = Ford("focus", "white", 2020, "Auto", False)

# Call class method to print car information
Car.print_cars([ford1])

