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
    """
    This is the abstract class for Enclosure. It features the abstract method for accepted animals, which is specifically assigned to each child class.
    """
    # Class attributes for size options and capacity, using list and dictionary
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
        """
        This is the abstract method for accepted animals.
        :param animal:
        :return:
        """
        pass

    def get_capacity(self):
        """
        This function gets the capacity of the enclosure
        :return: self.SIZE_CAPACITY[self.__size]: int
        """
        return self.SIZE_CAPACITY[self.__size]

    # Set the property for capacity
    capacity = property(get_capacity)

    def add_animal(self, animal):
        """
        This method adds an animal to an enclosure.
        :param animal:
        :return:
        """
        # The method first tests if an animal class is passed in (ie, a member of the staff class could not be added)
        if not isinstance(animal, Animal):
            print("Only animals can be added to the enclosure.\n")
            return
        # If there are no animals in the self.__animals list attribute, assign the animal type to that animal's species
        if len(self.__animals) == 0:
            self.__animal_type = animal.species
            # Append the animal to the animals attribute list and display result to the user
            self.__animals.append(animal)
            print(f"{animal.animal_name} the {animal.species} is now in the enclosure.\n")
        else:
            # If the length of te list is less than the capacity of the enclosure, enter if block
            if len(self.__animals) < self.capacity:
                # if the species is the same as the assigned animal type (ie, only the same animals can be added to the enclosure), append the animal to the enclosure and display result to user
                if animal.species == self.__animal_type:
                    self.__animals.append(animal)
                    print(f"{animal.animal_name.capitalize()} the {animal.species.capitalize()} has been introduced into the enclosure.\n")
                else:
                    # If the species and animal type do not match, display that the animal passed in could not be added to the enclosure
                    print(f"{animal.species.capitalize()}(s) don't get along with {self.__animal_type.capitalize()}(s) - best to keep them apart.\n")
            else:
                # if the enclosure is at capacity, display result to user
                print("The enclosure is at capacity - please expand the enclosure before adding additional animals.\n")

    def expand_enclosure(self):
        """
        This function expands the capacity of the enclosure
        :return:
        """
        # Assign the current index of the size options to variable index
        index = self.SIZE_OPTIONS.index(self.__size)
        # If the index is one less than the length of the list, display to user that they are already at the maximum capacity
        if index == len(self.SIZE_OPTIONS) - 1:
            print("The enclosure is already at maximum size.\n")
        else:
            # Otherwise, assign the size to the next option in the size options listm and display the result to the user
            self.__size = self.SIZE_OPTIONS[index + 1]
            print(f"The enclosure now has a capacity of {self.capacity}\n")

    def get_fed(self):
        """
        This is a getter for fed
        :return: self.__fed: boolean
        """
        return self.__fed

    # Set property for fed
    fed = property(get_fed)

    def feed_enclosure(self, staff_member):
        """
        This method allows a staff member to feed the enclosure. It takes a staff member, and does validation checks before feeding the enclosure.
        :param staff_member:
        :return:
        """
        # If the staff member passed in is a zookeeper, continue into the next if block
        if isinstance(staff_member, Zookeeper):
            # Check if the staff member is clocked in for work
            if staff_member.working:
                # The next check looks at whether the enclosure has already been fed
                if not self.fed:
                    # for each animal in the enclosure, call the eat function which prints individualised statements dependent on the dietary needs
                    for animal in self.__animals:
                        animal.eat()
                    # Assign the fed attribute to True
                    self.__fed = True
                else:
                    # If already fed, display result to user
                    print(f"{staff_member.staff_name} has already fed the animals in this enclosure today.\n")
            else:
                # If staff member is not clocked in for work, display result to user
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!\n")
        else:
            # If the wrong staff type is passed in, display result to user
            print("Only Zookeepers can feed the animals.\n")

    def get_clean(self):
        """
        This is a getter for clean
        :return: self.__clean: boolean
        """
        return self.__clean

    # Set property for clean
    clean = property(get_clean)

    def clean_enclosure(self, staff_member):
        """
        This method takes in a staff member to clean the enclosure. It does various validation checks prior to executing
        :param staff_member:
        :return:
        """
        # Validation to ensure it is the zookeeper object
        if isinstance(staff_member, Zookeeper):
            # Validation check to see if the staff member is clocked on
            if staff_member.working:
                # If the enclosure hasn't already been cleaned, set the attribute to True
                if not self.clean:
                    self.__clean = True
                    # Display result to user
                    print(f"{staff_member.staff_name} has successfully cleaned the enclosure.\n")
                else:
                    # If the enclosure was already cleaned, display reuslt to user
                    print(f"{staff_member.staff_name} has already cleaned the enclosure today.\n")
            else:
                # If the staff member is not clocked on, display result to user
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!\n")
        else:
            # If the wrong staff object was passed in, display result to user
            print(f"Only Zookeepers can clean the enclosures.\n")

    def get_health_check(self):
        """
        This is a getter for health check
        :return: self.__health_check: boolean
        """
        return self.__health_check

    # Set property for health check
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
        """
        This method checks the health of the enclosure. It takes a staff member, and does various validation checks before resetting animal health
        :param staff_member:
        :return:
        """
        # If the staff object passed in is a veterinarian, continue into the next if block
        if isinstance(staff_member, Veterinarian):
            # Validation to ensure staff member is clocked in
            if staff_member.working:
                # If the enclosure hasn't already been checked, continue into the loop
                if not self.health_check:
                    # For each animal in the enclosure, enter if-else block
                    for animal in self.__animals:
                        # If the animal health status is not "Healthy", display the current health of the animal
                        if animal.health != "Healthy":
                            print(f"{animal.animal_name} is currently {animal.health}")
                            # Reset the animal health
                            animal.set_health()
                            # Display the result to the user
                            print(f"{animal.animal_name} has been treated by {staff_member.staff_name}\n")
                        else:
                            # If the animal health status is healthy, display result to user
                            print(f"{animal.animal_name} is currently healthy!\n")
                    # Set boolean to True
                    self.__health_check = True
                else:
                    # If the enclosure has already been tended to, display result to user
                    print(f"{staff_member.staff_name} has already tended to this enclosure today.\n")
            else:
                # If the staff member is not clocked in for work, display result to user
                print(f"{staff_member.staff_name} is not clocked in for work - please clock in first!\n")
        else:
            # If the wrong staff object was passed in, display result to user
            print("Only Veterinarians can treat animals.\n")

    def health_report(self):
        """
        This function represents a health report for the animals in the enclosure
        :return:
        """
        # Create variable for the current date
        current_date = date.today()
        # Display header of the report using the current date
        print(f"Health Report: {current_date}")
        # Enter for loop to display health status for each animal
        for animal in self.__animals:
            # Display report to user
            print(f"Name: {animal.animal_name.capitalize()} >> Species: {animal.species.capitalize()} >> Health Status: {animal.health}")
        print()

    def get_animal_type(self):
        """
        This is a getter for animal type of the enclosure
        :return: self.__animal_type: str
        """
        return self.__animal_type.capitalize()

    # Set property for animal type
    animal_type = property(get_animal_type)

    def __str__(self):
        """
        This is the string method for enclosure
        :return: str
        """
        # Create a variable for the animal list, which loops through the list attribute and joins animals into a string
        animal_list = ", ".join(str(animal.get_name()) for animal in self.__animals)

        # Set fed variable to yes or no depending on boolean
        if self.__fed:
            animals_fed = "Yes"
        else:
            animals_fed = "No"
        # Set clean variable to yes or no depending on boolean
        if self.__clean:
            enclosure_clean = "Yes"
        else:
            enclosure_clean = "No"
        # Set health check variable to yes or no depending on boolean
        if self.__health_check:
            health_check = "Yes"
        else:
            health_check = "No"
        # Return the "report"
        return f"\nAnimals in this enclosure: {animal_list}\nAnimal Type: {self.animal_type}\nAnimals Fed: {animals_fed}\nEnclosure Clean: {enclosure_clean}\nHealth Checked: {health_check}\nCapacity: {self.SIZE_CAPACITY[self.__size]}\n"

class Aquatic(Enclosure):
    """
    This is a child class of enclosure
    """
    def __init__(self):
        # Set the attribute for accepted species in this enclosure type
        self.__accepted_species = {"fish", "seal", "shark", "dolphin", "turtle", "jellyfish", "crab", "lobster",
                                   "seahorse", "penguin", "walrus", "platypus"}
        super().__init__()

    def can_accept(self, animal):
        """
        This method takes in an animal as a parameter, and checks membership in the accepted species attribute
        :param animal:
        :return: boolean
        """
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        """
        This function determines whether the animal can be accepted into the enclosure type and displays result to user
        :param animal:
        :return:
        """
        # If the result of the can_accept function is True, use super to call upon the parent class add animal function
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            # Display to user that the species cannot be added to this type of enclosure
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")

class Savannah(Enclosure):
    """
    This is a child class of enclosure
    """
    def __init__(self):
        # Set the attribute for accepted species in this enclosure type
        self.__accepted_species = {"giraffe", "zebra", "elephant", "antelope", "buffalo", "hippopotamus", "lion",
                                   "cheetah", "hyena", "leopard", "meerkat", "ostrich", "monkey", "gorilla",
                                   "orangutan", "rhinoceros"}
        super().__init__()

    def can_accept(self, animal):
        """
        This method takes in an animal as a parameter, and checks membership in the accepted species attribute
        :param animal:
        :return: boolean
        """
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        """
        This function determines whether the animal can be accepted into the enclosure type and displays result to user
        :param animal:
        :return:
        """
        # If the result of the can_accept function is True, use super to call upon the parent class add animal function
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            # Display to user that the species cannot be added to this type of enclosure
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")

class Vivarium(Enclosure):
    """
    This is a child class of enclosure
    """
    def __init__(self):
        # Set the attribute for accepted species in this enclosure type
        self.__accepted_species = {"snake", "lizard", "spider", "frog", "insect", "dragon"}
        super().__init__()

    def can_accept(self, animal):
        """
        This method takes in an animal as a parameter, and checks membership in the accepted species attribute
        :param animal:
        :return: boolean
        """
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        """
        This function determines whether the animal can be accepted into the enclosure type and displays result to user
        :param animal:
        :return:
        """
        # If the result of the can_accept function is True, use super to call upon the parent class add animal function
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            # Display to user that the species cannot be added to this type of enclosure
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")

class Aviary(Enclosure):
    """
    This is a child class of enclosure
    """
    def __init__(self):
        # Set the attribute for accepted species in this enclosure type
        self.__accepted_species = {"bird", "parrot", "bat", "duck", "goose"}
        super().__init__()

    def can_accept(self, animal):
        """
        This method takes in an animal as a parameter, and checks membership in the accepted species attribute
        :param animal:
        :return: boolean
        """
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        """
        This function determines whether the animal can be accepted into the enclosure type and displays result to user
        :param animal:
        :return:
        """
        # If the result of the can_accept function is True, use super to call upon the parent class add animal function
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            # Display to user that the species cannot be added to this type of enclosure
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")

class Farmyard(Enclosure):
    """
    This is a child class of enclosure
    """
    def __init__(self):
        # Set the attribute for accepted species in this enclosure type
        self.__accepted_species = {"dog", "cat", "cow", "sheep", "pig", "horse", "goat", "chicken", "donkey"}
        super().__init__()

    def can_accept(self, animal):
        """
        This method takes in an animal as a parameter, and checks membership in the accepted species attribute
        :param animal:
        :return: boolean
        """
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        """
        This function determines whether the animal can be accepted into the enclosure type and displays result to user
        :param animal:
        :return:
        """
        # If the result of the can_accept function is True, use super to call upon the parent class add animal function
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            # Display to user that the species cannot be added to this type of enclosure
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")

class Bushland(Enclosure):
    """
    This is a child class of enclosure
    """
    def __init__(self):
        # Set the attribute for accepted species in this enclosure type
        self.__accepted_species = {"koala", "kangaroo", "echidna", "wallaby", "wombat", "emu", "possum",
                                   "tasmanian devil", "dingo", "quokka"}
        super().__init__()

    def can_accept(self, animal):
        """
        This method takes in an animal as a parameter, and checks membership in the accepted species attribute
        :param animal:
        :return: boolean
        """
        return animal.species.lower() in self.__accepted_species

    def add_animal(self, animal):
        """
        This function determines whether the animal can be accepted into the enclosure type and displays result to user
        :param animal:
        :return:
        """
        # If the result of the can_accept function is True, use super to call upon the parent class add animal function
        if self.can_accept(animal):
            super().add_animal(animal)
        else:
            # Display to user that the species cannot be added to this type of enclosure
            print(f"{animal.species.capitalize()}(s) do not belong in this enclosure\n")
