"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""


class Animal:
    def __init__(self, name, species, age, dietary_needs):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs

    def get_name(self):
        return self.__name

    animal_name = property(get_name)

    def get_dietary_needs(self):
        return self.__dietary_needs

    diet = property(get_dietary_needs)

    def cry(self):
        return f"{self.animal_name} is crying!"

    def eat(self):
        food = ""
        if self.diet == "Herbivore":
            food = "tasty greens"
        elif self.diet == "Omnivore":
            food = "a scrumptious mix of greens and meat"
        elif self.diet == "Carnivore":
            food = "a hearty portion of meat"
        return f"{self.animal_name} is currently eating {food}"

    def sleep(self):
        return f"{self.animal_name} is sleeping..."


class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)


    def cry(self):
        return super().cry() + " *Bleat Bleat*"

    def eat(self):
        return super().eat()

    def sleep(self):
        return super().sleep()


class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def cry(self):
        return super().cry() + " *Hiss Hiss*"

    def eat(self):
        return super().eat()

    def sleep(self):
        return super().sleep()


class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def cry(self):
        return super().cry() + " *Chirp Chirp*"

    def eat(self):
        return super().eat()

    def sleep(self):
        return super().sleep()


"""animal = Mammal("Caramello", "Koala", 5, "Herbivore")
print(animal.cry())
print(animal.eat())
print(animal.sleep())"""