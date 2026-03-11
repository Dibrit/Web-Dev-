class Animal:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        return f"{self.name} is eating"

    def make_sound(self):
        return f"{self.name} makes a sound"

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Weight: {self.weight}"


class Dog(Animal):

    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def make_sound(self):
        return f"{self.name} barks"

    def fetch(self):
        return f"{self.name} is fetching the ball"

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}, Age: {self.age}"


class Cat(Animal):

    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color

    def make_sound(self):
        return f"{self.name} meows"

    def scratch(self):
        return f"{self.name} is scratching"

    def __str__(self):
        return f"Cat: {self.name}, Color: {self.color}, Age: {self.age}"