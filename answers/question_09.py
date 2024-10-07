class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

dog1 = Dog("Tommy", "Labrador")
print(dog1.make_sound())
dog1.fetch()