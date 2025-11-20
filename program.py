"""
File: program.py
Description: This file holds test modules
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from animal import Mammal
from animal import Bird
from animal import Reptile
from animal import Fish
from enclosure import Bushland
from staff import Zookeeper
from staff import Veterinarian

class TestZoo:
    @pytest.fixture
    def mammal(self):
        return Mammal("Caramello", "koala", 5, "herbivore")

    @pytest.fixture
    def bird(self):
        return Bird("Tweety", "bird", 7, "omnivore")

    @pytest.fixture
    def fish(self):
        return Fish("Nemo", "fish", 9, "omnivore")

    @pytest.fixture
    def reptile(self):
        return Reptile("Rango", "lizard", 14, "carnivore")



    @pytest.fixture
    def bushland(self):
        return Bushland()

    @pytest.fixture
    def zookeeper(self):
        return Zookeeper("Bill")

    @pytest.fixture
    def vet(self):
        return Veterinarian("Ben")

    # Tests for Animal Class

    def test_get_name(self, mammal, bird, fish, reptile):
        assert mammal.animal_name == "Caramello"
        assert bird.animal_name == "Tweety"
        assert fish.animal_name == "Nemo"
        assert reptile.animal_name == "Rango"

    def test_get_age(self, mammal, bird, fish, reptile):
        assert mammal.age == 5
        assert mammal.age != "5"
        assert bird.age == 7
        assert bird.age != "7"
        assert fish.age == 9
        assert fish.age != "9"
        assert reptile.age == 14
        assert reptile.age != "14"

    def test_get_dietary_needs(self, mammal, bird, fish, reptile):
        assert mammal.diet == "Herbivore"
        assert bird.diet == "Omnivore"
        assert fish.diet == "Omnivore"
        assert reptile.diet == "Carnivore"

    def test_get_species(self, mammal, bird, fish, reptile):
        assert mammal.species == "koala"
        assert bird.species == "bird"
        assert fish.species == "fish"
        assert reptile.species == "lizard"

    def test_get_health(self, mammal, bird, fish, reptile):
        assert mammal.get_health() == "Healthy"
        assert bird.get_health() == "Healthy"
        assert fish.get_health() == "Healthy"
        assert reptile.get_health() == "Healthy"

    def test_health_status(self, mammal, bird, fish, reptile):
        assert mammal.health_status() == "Healthy" or "Injured" or "Sick" or "Behaviourally Challenged"
        assert bird.health_status() == "Healthy" or "Injured" or "Sick" or "Behaviourally Challenged"
        assert fish.health_status() == "Healthy" or "Injured" or "Sick" or "Behaviourally Challenged"
        assert reptile.health_status() == "Healthy" or "Injured" or "Sick" or "Behaviourally Challenged"


    def test_str(self, mammal, bird, fish, reptile):
        assert mammal.__str__() == "Meet Caramello! Caramello is a koala, and is 5 years old. Caramello is a Herbivore.\nTo learn more about Caramello, ask one of our friendly Zookeepers!\n"
        assert bird.__str__() == "Meet Tweety! Tweety is a bird, and is 7 years old. Tweety is a Omnivore.\nTo learn more about Tweety, ask one of our friendly Zookeepers!\n"
        assert fish.__str__() == "Meet Nemo! Nemo is a fish, and is 9 years old. Nemo is a Omnivore.\nTo learn more about Nemo, ask one of our friendly Zookeepers!\n"
        assert reptile.__str__() == "Meet Rango! Rango is a lizard, and is 14 years old. Rango is a Carnivore.\nTo learn more about Rango, ask one of our friendly Zookeepers!\n"


    # Tests for Enclosure Class

    def test_get_capacity(self, bushland):
        assert bushland.capacity == 6

    def test_can_accept(self, bushland, mammal):
        assert bushland.can_accept(mammal) == True

    def test_get_fed(self, bushland):
        assert bushland.fed == False

    def test_get_clean(self, bushland):
        assert bushland.clean == False

    def test_get_health_check(self, bushland):
        assert bushland.health_check == False

