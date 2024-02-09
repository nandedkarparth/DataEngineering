class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog(name="Buddy", age=3)

print(f"My dog's name is {my_dog.name} and it is {my_dog.age} years old.")
my_dog.bark()
