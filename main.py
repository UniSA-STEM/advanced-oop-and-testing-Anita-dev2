"""
File: main.py
Description: main file
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Fish
from animal import Bird
from animal import Reptile
from animal import Mammal
from enclosure import Aviary
from enclosure import Vivarium
from enclosure import Aquatic
from enclosure import Savannah
from enclosure import Bushland
from enclosure import Farmyard
from staff import Zookeeper
from staff import Veterinarian


def animal_methods():
    """
    This function shows the basic functionality of creating an animal and enclosure.
    The animal is added to the enclosure, and the functionality of the methods eat and cry are shown.
    :return:
    """
    # Create an enclosure
    aquarium = Aquatic()
    # Instantiate a Fish object
    fish = Fish("Nemo", "fish", 5, "omnivore")
    # Add the fish to the enclosure
    aquarium.add_animal(fish)
    # Method for cry
    fish.cry()
    # Method for eating
    fish.eat()
    # Display enclosure object
    print(aquarium)
    # Display fish object
    print(fish)

def adding_different_animals():
    """
    This function tests adding various types and species of animal to the same enclosure.
    It first adds the correct type to an enclosure, then attempts to add a different species to the same enclosure.
    It then tries to add a different type to the same enclosure.
    :return:
    """
    # Instantiate a Bird object
    bird = Bird("Tweety", "bird", 6, "omnivore")
    # Instantiate an aviary object
    aviary = Aviary()
    # Add the bird object to the aviary object
    aviary.add_animal(bird)

    # Instantiate second bird object of different species
    bird2 = Bird("Daffy", "duck", 3, "carnivore")
    # Try to add bird to same aviary
    aviary.add_animal(bird2)

    # Create reptile object
    lizard = Reptile("Rango", "lizard", 13, "carnivore")
    # Attempt to add lizard to aviary
    aviary.add_animal(lizard)

def staff_methods():
    """
    This function instantiates two staff members. It then prints their staff id numbers.
    It then displays the string method for staff, and demonstrates the clock in and out function.
    :return:
    """
    # Create two staff members of different roles
    staff1 = Zookeeper("Bill")
    staff2 = Veterinarian("Ben")

    # Prints staff id to user
    print(staff1.staff_id)
    print(staff2.staff_id)

    # Display staff object to user
    print(staff1)
    print(staff2)

    # Staff members clocking in
    staff1.clock_in()
    staff2.clock_in()
    # Staff 2 attempting a second clock in
    staff2.clock_in()
    # Staff member clocking out
    staff1.clock_out()


animal_methods()
adding_different_animals()
staff_methods()



"""staff1 = Zookeeper("Sally", 2,)
aquarium.feed_enclosure(staff1)
staff1.clock_in()
aquarium.feed_enclosure(staff1)
aquarium.feed_enclosure(staff1)
print(aquarium)
aquarium.clean_enclosure(staff1)
print(aquarium)"""

"""aviary = Aviary()
bird = Bird("Billy", "Bird", 6, "Carnivore")
aviary.add_animal(bird)
bird1 = Bird("Bab", "Bird", 4, "Omnivore")
aviary.add_animal(bird1)
print(aviary)

staff1 = Zookeeper("Sally")
staff2 = Veterinarian("Chris")
staff2.clock_in()
aviary.check_health(staff2)
aviary.check_health(staff2)
print(aviary)

aviary.feed_enclosure(staff1)
print(aviary)
staff1.clock_in()
aviary.feed_enclosure(staff1)
"""