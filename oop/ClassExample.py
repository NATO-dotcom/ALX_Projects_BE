class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        return f"{self.name} says woof!"
    def dogAge(self):
        return self.age

my_dog=Dog("broskii",15)
print(my_dog.bark())
print(my_dog.dogAge())