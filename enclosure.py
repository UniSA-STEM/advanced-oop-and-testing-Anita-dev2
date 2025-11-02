"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from animal import Fish
from animal import Bird
from animal import Reptile
from animal import Mammal
from staff import Staff
from staff import Zookeeper
from staff import Veterinarian

# Make a dictionary or to hold values accepted per size of enclosure
# also make one for environment per animal type

class Enclosure:
    def __init__(self):
        self.__fed = False
        self.__clean = False
        self.__animals = []
        self.__animal_type = None


    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            print("Only animals can be added to the enclosure.")
            return

        if len(self.__animals) == 0:
            self.__animal_type = animal.species
            self.__animals.append(animal)
            print(f"{animal.animal_name} the {animal.species} is now in the enclosure. ")
        else:
            if animal.species == self.__animal_type:
                self.__animals.append(animal)
                print(f"{animal.animal_name} the {animal.species} has been introduced into the enclosure.")
            else:
                print(f"{animal.species}(s) don't get along with {self.__animal_type}(s) - best to keep them apart.")

    def get_fed(self):
        return self.__fed

    fed = property(get_fed)

    def feed_enclosure(self, staff_member):
        if staff_member.working:
            if isinstance(staff_member, Zookeeper):
                if not self.fed:
                    for animal in self.__animals:
                        animal.eat()
                    self.__fed = True
                else:
                    print(f"{staff_member.staff_name} has already fed the animals in this enclosure today.")
            else:
                print("Only Zookeepers can feed the animals.")
        else:
            print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!")



class Aquatic(Enclosure):
    def __init__(self):
        super().__init__()


    def add_animal(self, animal):
        if not isinstance(animal, Fish):
            print(f"{animal.species} cannot live in this enclosure. Only Fish can live in the Aquarium.")

        super().add_animal(animal)

class Savannah(Enclosure):
    def __init__(self):
        super().__init__()

    def add_animal(self, animal):
        if not isinstance(animal, Mammal):
            print(f"{animal.species} cannot live in this enclosure. Only Mammals can live in the Savannah.")

        super().add_animal(animal)


class Vivarium(Enclosure):
    def __init__(self):
        super().__init__()

    def add_animal(self, animal):
        if not isinstance(animal, Reptile):
            print(f"{animal.species} cannot live in this enclosure. Only Reptiles can live in the Vivarium.")

        super().add_animal(animal)


class Aviary(Enclosure):
    def __init__(self):
        super().__init__()

    def add_animal(self, animal):
        if not isinstance(animal, Bird):
            print(f"{animal.species} cannot live in this enclosure. Only Birds can live in the Aviary.")

        super().add_animal(animal)



