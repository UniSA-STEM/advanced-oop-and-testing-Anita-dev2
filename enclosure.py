"""
File: enclosure.py
Description: This module represents the enclosure class and its children classes
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from datetime import date
from animal import Animal
from animal import Fish
from animal import Bird
from animal import Reptile
from animal import Mammal
from staff import Zookeeper
from staff import Veterinarian


class Enclosure(ABC):
    SIZE_OPTIONS = ["small", "medium", "large"]
    SIZE_CAPACITY = {
        "small": 6,
        "medium": 12,
        "large": 18
    }

    def __init__(self):
        self.__fed = False
        self.__clean = False
        self.__health_check = False
        self.__animals = []
        self.__animal_type = None
        self.__size = "small"

    @abstractmethod
    def can_accept(self, animal):
        pass

    def get_capacity(self):
        return self.SIZE_CAPACITY[self.__size]

    capacity = property(get_capacity)

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            print("Only animals can be added to the enclosure.\n")
            return

        if len(self.__animals) == 0:
            self.__animal_type = animal.species
            self.__animals.append(animal)
            print(f"{animal.animal_name} the {animal.species} is now in the enclosure.\n")
        else:
            if len(self.__animals) < self.capacity:
                if animal.species == self.__animal_type:
                    self.__animals.append(animal)
                    print(
                        f"{animal.animal_name.capitalize()} the {animal.species.capitalize()} has been introduced into the enclosure.\n")
                else:
                    print(
                        f"{animal.species.capitalize()}(s) don't get along with {self.__animal_type.capitalize()}(s) - best to keep them apart.\n")
            else:
                print("The enclosure is at capacity - please expand the enclosure before adding additional animals.\n")

    def expand_enclosure(self):
        index = self.SIZE_OPTIONS.index(self.__size)

        if index == len(self.SIZE_OPTIONS) - 1:
            print("The enclosure is already at maximum size.\n")
        else:
            self.__size = self.SIZE_OPTIONS[index + 1]
            print(f"The enclosure now has a capacity of {self.capacity}\n")

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
                    print(f"{staff_member.staff_name} has already fed the animals in this enclosure today.\n")
            else:
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!\n")
        else:
            print("Only Zookeepers can feed the animals.\n")

    def get_clean(self):
        return self.__clean

    clean = property(get_clean)

    def clean_enclosure(self, staff_member):
        if isinstance(staff_member, Zookeeper):
            if staff_member.working:
                if not self.clean:
                    self.__clean = True
                    print(f"{staff_member.staff_name} has successfully cleaned the enclosure.\n")
                else:
                    print(f"{staff_member.staff_name} has already cleaned the enclosure today.\n")
            else:
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!\n")
        else:
            print(f"Only Zookeepers can clean the enclosures.\n")

    def get_health_check(self):
        return self.__health_check

    health_check = property(get_health_check)

    def generate_health(self):
        """
        This function generates a health status for each animal in the enclosure list, and sets the status to the animal attribute
        :return:
        """
        # Iterate through enclosure list of animals and assign health status
        for animal in self.__animals:
            animal.get_health = animal.health_status()

    def check_health(self, staff_member):
        if isinstance(staff_member, Veterinarian):
            if staff_member.working:
                if not self.health_check:
                    for animal in self.__animals:
                        if animal.health != "Healthy":
                            print(f"{animal.animal_name} is currently {animal.health}")
                            animal.set_health()
                            print(f"{animal.animal_name} has been treated by {staff_member.staff_name}\n")
                        else:
                            print(f"{animal.animal_name} is currently healthy!\n")

                    self.__health_check = True
                else:
                    print(f"{staff_member.staff_name} has already tended to this enclosure today.\n")
            else:
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!\n")
        else:
            print("Only Veterinarians can treat animals.\n")

    def health_report(self):
        current_date = date.today()
        print(f"Health Report: {current_date}")
        for animal in self.__animals:
            print(
                f"Name: {animal.animal_name.capitalize()} >> Species: {animal.species.capitalize()} >> Health Status: {animal.health}")
        print()

    def get_animal_type(self):
        return self.__animal_type.capitalize()

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

        return f"\nAnimals in this enclosure: {animal_list}\nAnimal Type: {self.animal_type}\nAnimals Fed: {animals_fed}\nEnclosure Clean: {enclosure_clean}\nHealth Checked: {health_check}\nCapacity: {self.SIZE_CAPACITY[self.__size]}\n"


class Aquatic(Enclosure):
    def __init__(self):
        self.__accepted_species = {"fish", "seal", "shark", "dolphin", "turtle", "jellyfish", "crab", "lobster",
                                   "seahorse", "penguin", "walrus", "platypus"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")


class Savannah(Enclosure):
    def __init__(self):
        self.__accepted_species = {"giraffe", "zebra", "elephant", "antelope", "buffalo", "hippopotamus", "lion",
                                   "cheetah", "hyena", "leopard", "meerkat", "ostrich", "monkey", "gorilla",
                                   "orangutan", "rhinoceros"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")


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
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")


class Aviary(Enclosure):
    def __init__(self):
        self.__accepted_species = {"bird", "parrot", "bat", "duck", "goose"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")


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
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")


class Bushland(Enclosure):
    def __init__(self):
        self.__accepted_species = {"koala", "kangaroo", "echidna", "wallaby", "wombat", "emu", "possum",
                                   "tasmanian devil", "dingo", "quokka"}
        super().__init__()

    def can_accept(self, animal):
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")
