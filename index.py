class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of Person
person = Person("Alice", 30, "Female")

# Calling the introduce method
person.introduce()
