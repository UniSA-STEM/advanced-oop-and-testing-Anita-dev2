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


def staff_tending():
    """
    This function shows the functionality of the staff. It demonstrates staff feeding, doing health checks and cleaning enclosures.
    :return:
    """
    # Instantiate an enclosure
    enclosure = Savannah()

    # Instantiate both staff types
    keeper = Zookeeper("Bill")
    vet = Veterinarian("Ben")

    # Create two lion "Mammal" objects and add to enclosure
    lion = Mammal("Simba", "lion", 6, "carnivore")
    lion2 = Mammal("Scar", "lion", 10, "carnivore")
    enclosure.add_animal(lion)
    enclosure.add_animal(lion2)

    # Feed the enclosure without staff clocking in
    enclosure.feed_enclosure(keeper)

    # Staff clock in
    keeper.clock_in()
    vet.clock_in()

    # Attempt to feed enclosure after clock in
    enclosure.feed_enclosure(keeper)

    # Attempt for the vet to feed enclosure
    enclosure.feed_enclosure(vet)

    # Keeper to clean enclosure
    enclosure.clean_enclosure(keeper)

    # Generate enclosure health statuses
    enclosure.generate_health()

    # Display health report
    enclosure.health_report()

    # Vet checks health of animals in enclosure
    enclosure.check_health(vet)

    # Display health report again after health checks
    enclosure.health_report()

    # Attempt to clean enclosure by vet and again by keeper
    enclosure.clean_enclosure(vet)
    enclosure.clean_enclosure(keeper)

    # Show status report of enclosure
    print(enclosure)


def expanding_enclosure():
    """
    This function showcases the sizes of enclosure and the functionality of expanding the enclosure.
    :return:
    """
    # Instantiate a farmyard enclosure
    farmyard = Farmyard()

    # Create 6 Mammal objects and add all to the enclosure
    dog1 = Mammal("Scooby", "dog", 9, "omnivore")
    dog2 = Mammal("Bluey", "dog", 3, "omnivore")
    dog3 = Mammal("Clifford", "dog", 4, "omnivore")
    dog4 = Mammal("Slinky", "dog", 2, "omnivore")
    dog5 = Mammal("Snoopy", "dog", 7, "omnivore")
    dog6 = Mammal("Lassie", "dog", 2, "omnivore")
    farmyard.add_animal(dog1)
    farmyard.add_animal(dog2)
    farmyard.add_animal(dog3)
    farmyard.add_animal(dog4)
    farmyard.add_animal(dog5)
    farmyard.add_animal(dog6)

    # Display enclosure stats/report
    print(farmyard)

    # Attempt to add another valid animal
    dog7 = Mammal("Bingo", "dog", 5, "omnivore")
    farmyard.add_animal(dog7)

    # Expand the enclosure, and re-add the valid animal
    farmyard.expand_enclosure()
    farmyard.add_animal(dog7)

    # Display enclosure stats/report
    print(farmyard)

    # Expand and display again
    farmyard.expand_enclosure()
    print(farmyard)

    # Try to expand after max expansions
    farmyard.expand_enclosure()


if __name__ == "__main__":
    animal_methods()
    adding_different_animals()
    staff_methods()
    staff_tending()
    expanding_enclosure()
