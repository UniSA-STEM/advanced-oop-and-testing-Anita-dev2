"""
File: enclosure.py
Description: This module represents the enclosure class and its children classes
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from animal import Animal
from animal import Fish
from animal import Bird
from animal import Reptile
from animal import Mammal
from staff import Zookeeper
from staff import Veterinarian

class Enclosure:
    def __init__(self):
        self.__fed = False
        self.__clean = False
        self.__health_check = False
        self.__animals = []
        self.__animal_type = None

    @abstractmethod
    def can_accept(self, animal):
        pass

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
        if isinstance(staff_member, Zookeeper):
            if staff_member.working:
                if not self.fed:
                    for animal in self.__animals:
                        animal.eat()
                    self.__fed = True
                else:
                    print(f"{staff_member.staff_name} has already fed the animals in this enclosure today.")
            else:
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!")
        else:
            print("Only Zookeepers can feed the animals.")

    def get_clean(self):
        return self.__clean

    clean = property(get_clean)

    def clean_enclosure(self, staff_member):
        if isinstance(staff_member, Zookeeper):
            if staff_member.working:
                if not self.clean:
                    self.__clean = True
                    print(f"{staff_member.staff_name} has successfully cleaned the enclosure.")
                else:
                    print(f"{staff_member.staff_name} has already cleaned the enclosure today.")
            else:
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!")
        else:
            print(f"Only Zookeepers can clean the enclosures.")

    def get_health_check(self):
        return self.__health_check

    health_check = property(get_health_check)

    def check_health(self, staff_member):
        if isinstance(staff_member, Veterinarian):
            if staff_member.working:
                if not self.health_check:
                    for animal in self.__animals:
                        if animal.health_status != "Healthy":
                            print(f"{animal.animal_name} is currently {animal.health_status()}")
                            animal.set_health()
                            print(f"{animal.animal_name} has been treated by {staff_member.staff_name}")

                    self.__health_check = True
                else:
                    print(f"{staff_member.staff_name} has already tended to this enclosure today")
            else:
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!")
        else:
            print("Only Veterinarians can treat animals.")

    def get_animal_type(self):
        return self.__animal_type

    animal_type = property(get_animal_type)


    def __str__(self):
        animal_list = ", ".join(str(animal.get_name()) for animal in self.__animals)

        if self.__fed:
            animals_fed = "Yes"
        else:
            animals_fed = "No"

        if self.__clean:
            enclosure_clean = "Yes"
        else:
            enclosure_clean = "No"

        if self.__health_check:
            health_check = "Yes"
        else:
            health_check = "No"

        return f"\nAnimals in this enclosure: {animal_list}\nAnimal Type: {self.animal_type}\nAnimals Fed: {animals_fed}\nEnclosure Clean: {enclosure_clean}\nHealth Checked: {health_check}\n"



class Aquatic(Enclosure):
    def __init__(self):
        self.__accepted_species = {"fish", "seal", "shark", "dolphin", "turtle", "jellyfish", "crab", "lobster", "seahorse", "penguin", "walrus", "platypus"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species}(s) do not belong in this enclosure")

    def __str__(self):
        return super().__str__()

class Savannah(Enclosure):
    def __init__(self):
        self.__accepted_species = {"giraffe", "zebra", "elephant", "antelope", "buffalo", "hippopotamus", "lion", "cheetah", "hyena", "leopard", "meerkat", "ostrich"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species}(s) do not belong in this enclosure")

class Vivarium(Enclosure):
    def __init__(self):
        self.__accepted_species = {"snake", "lizard", "spider", "frog", "insect", "dragon"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species}(s) do not belong in this enclosure")


class Aviary(Enclosure):
    def __init__(self):
        self.__accepted_species = {"bird", "parrot", "bat"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species}(s) do not belong in this enclosure")


class Farmyard(Enclosure):
    def __init__(self):
        self.__accepted_species = {"dog", "cat", "cow", "sheep", "pig", "horse", "goat", "chicken", "donkey"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species}(s) do not belong in this enclosure")

class Australiana(Enclosure):
    def __init__(self):
        self.__accepted_species = {"koala", "kangaroo", "echidna", "wallaby", "wombat", "emu", "possum", "tasmanian devil", "dingo", "quokka"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species}(s) do not belong in this enclosure")





"""fish = Fish("dory", "seal", 4, "herbivore")
aqua1 = Aquatic()
aqua1.add_animal(fish)"""
"""fish2 = Fish("nemo", "fish", 5, "herbivore")
aqua1.add_animal(fish2)
print(aqua1)"""

lion = Mammal("hello", "lion", 5, "carnivore")
aqua1 = Aquatic()
aqua1.add_animal(lion)