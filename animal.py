"""
File: animal.py
Description: This module represents the abstract animal classes and the child classes associated with animal
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""
import random
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    The animal class is an abstract class. It takes name, species, age and dietary needs as parameters for attributes.
    It also has a health attribute, which is initialised as "Healthy". The class has an abstract method of cry.
    It has other methods which include health status, eat and sleep.
    """
    def __init__(self, name, species, age, dietary_needs):

        # Validate name input
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.__name = name

        # Validate species input
        if not isinstance(species, str):
            raise TypeError("Species must be a string.")
        self.__species = species

        # Validate age input
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0:
            raise ValueError("Age cannot be less than 0")
        self.__age = age

        # Validate dietary_needs input
        valid_diet = {"carnivore", "omnivore", "herbivore"}
        if dietary_needs.lower() not in valid_diet:
            raise ValueError(f"Valid diets include: {', '.join(valid_diet)}")

        self.__dietary_needs = dietary_needs

        # If the input passes all validation, it is assigned into the attributes
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health = "Healthy"

    def get_name(self):
        """
        This is a getter for name
        :return: name: str
        """
        return self.__name.capitalize()

    # Set property for animal name
    animal_name = property(get_name)

    def get_age(self):
        """
        This is a getter for age
        :return: age: int
        """
        return self.__age

    # Set property for animal age
    age = property(get_age)

    def get_dietary_needs(self):
        """
        This is a getter for dietary needs
        :return: dietary_needs: str
        """
        return self.__dietary_needs.capitalize()

    # Set property for dietary needs
    diet = property(get_dietary_needs)

    def get_species(self):
        """
        This is a getter for species
        :return: species
        """
        return self.__species

    # Set property for species
    species = property(get_species)

    def get_health(self):
        """
        This is a getter for health
        :return: health
        """
        return self.__health

    def set_health(self):
        """
        This is a setter for health to reset an animal's health back to healthy
        :return: health
        """
        self.__health = "Healthy"

    # Set property for health
    health = property(get_health, set_health)

    def health_status(self):
        """
        This function uses the random feature to create a number between 1 and 4.
        It then assigns that number to a health status for the animal.
        :return: health
        """
        # set status to a random integer between 1 and 4
        status = random.randint(1, 4)
        # assign status depending on random result
        if status == 1:
            self.__health = "Healthy"
        elif status == 2:
            self.__health = "Sick"
        elif status == 3:
            self.__health = "Injured"
        elif status == 4:
            self.__health = "Behaviourally Challenged"

        return self.__health

    # Create abstract method for cry to be used in child classes
    @abstractmethod
    def cry(self):
        pass

    def eat(self):
        """
        This function takes the dietary needs of the animal, and sets a specific string output depending on the diet.
        The function prints the animal name and what they are eating, with the specified string
        :return:
        """
        # Initialise food variable
        food = ""
        # Run checks to see which dietary need the animal has, and print the relevant statement
        if self.diet == "Herbivore":
            food = "tasty greens."
        elif self.diet == "Omnivore":
            food = "a scrumptious mix of greens and meat."
        elif self.diet == "Carnivore":
            food = "a hearty portion of meat."
        # Display result of the function to user
        print(f"{self.animal_name} is currently eating {food}.\n")

    def sleep(self):
        """
        This function takes the animal name and prints a string to the user to denote the animal is sleeping
        :return:
        """
        # Display result of the function to the user
        print(f"{self.animal_name} is sleeping...\n")


    def __str__(self):
        """
        This is the string method for Animal
        :return:
        """
        return f"Meet {self.animal_name}! {self.animal_name} is a {self.species}, and is {self.age} years old. {self.animal_name} is a {self.diet}.\nTo learn more about {self.animal_name}, ask one of our friendly Zookeepers!\n"


class Mammal(Animal):
    """
    This is a child class of Animal. It inherits the constructor and all functions, except for cry which it overrides
    """
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)


    def cry(self):
        """
        This function takes the animal name and prints the specific animal cry to the user
        :return:
        """
        print(f"{self.animal_name} is crying! *Bleat Bleat*\n")


class Reptile(Animal):
    """
    This is a child class of animal. It inherits the constructor and all methods except for cry, which it overrides
    """
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def cry(self):
        """
        This function takes the animal name and prints the specific animal cry to the user
        :return:
        """
        print(f"{self.animal_name} is crying! *Hiss Hiss*\n")


class Bird(Animal):
    """
    This is a child class of animal. It inherits the constructor and all methods except for cry, which it overrides
    """
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def cry(self):
        """
        This function takes the animal name and prints the specific animal cry to the user
        :return:
        """
        print(f"{self.animal_name} is crying! *Chirp Chirp*\n")

class Fish(Animal):
    """
    This is a child class of animal. It inherits the constructor and all methods except for cry, which it overrides
    """
    def __init__(self, name, species, age, dietary_needs):
        super().__init__(name, species, age, dietary_needs)

    def cry(self):
        """
        This function takes the animal name and prints the specific animal cry to the user
        :return:
        """
        print(f"{self.animal_name} is crying! *Bubble Bubble*")

