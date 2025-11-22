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
from enclosure import Farmyard
from enclosure import Vivarium
from enclosure import Aviary
from enclosure import Aquatic
from enclosure import Savannah
from staff import Zookeeper
from staff import Veterinarian

class TestZoo:
    # Setting up with Fixtures

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
    def farmyard(self):
        return Farmyard()

    @pytest.fixture
    def vivarium(self):
        return Vivarium()

    @pytest.fixture
    def aviary(self):
        return Aviary()

    @pytest.fixture
    def aquatic(self):
        return Aquatic()

    @pytest.fixture
    def savannah(self):
        return Savannah()

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

    def test_name_type(self, mammal, bird, fish, reptile):
        assert isinstance(mammal.animal_name, str)
        assert isinstance(bird.animal_name, str)
        assert isinstance(fish.animal_name, str)
        assert isinstance(reptile.animal_name, str)

    def test_invalid_name(self, mammal):
        with pytest.raises(TypeError):
            Mammal(123, "lion", 5, "carnivore")

    def test_invalid_age(self, reptile):
        with pytest.raises(TypeError):
            Reptile("Rango", "lizard", "5", "carnivore")

        with pytest.raises(ValueError):
            Reptile("Rango", "lizard", -3, "carnivore")

        with pytest.raises(TypeError):
            Reptile("Rango", "lizard", "five", "carnivore")

    def test_invalid_species(self, fish):
        with pytest.raises(TypeError):
            Fish("Nemo", 3, 4, "omnivore")

    def test_invalid_dietary_needs(self, bird):
        with pytest.raises(ValueError):
            Bird("Tweety", "bird", 5, "vegetarian")

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

    def test_set_health(self, mammal):
        mammal.set_health()
        assert mammal.get_health() == "Healthy"

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

    def test_get_capacity(self, bushland, aviary, vivarium, farmyard, savannah, aquatic):
        assert bushland.capacity == 6
        assert aviary.capacity == 6
        assert vivarium.capacity == 6
        assert farmyard.capacity == 6
        assert savannah.capacity == 6
        assert aquatic.capacity == 6
        assert aquatic.capacity != "small"

    def test_can_accept(self, bushland, aviary, vivarium, farmyard, savannah, aquatic, mammal):
        assert bushland.can_accept(mammal) == True
        assert aviary.can_accept(mammal) == False
        assert vivarium.can_accept(mammal) == False
        assert farmyard.can_accept(mammal) == False
        assert savannah.can_accept(mammal) == False
        assert aquatic.can_accept(mammal) == False

    def test_get_fed(self, bushland, aviary, vivarium, farmyard, savannah, aquatic):
        assert bushland.fed == False
        assert aviary.fed == False
        assert vivarium.fed == False
        assert farmyard.fed == False
        assert savannah.fed == False
        assert aquatic.fed == False

    def test_get_clean(self, bushland, aviary, vivarium, farmyard, savannah, aquatic):
        assert bushland.clean == False
        assert aviary.clean == False
        assert vivarium.clean == False
        assert farmyard.clean == False
        assert savannah.clean == False
        assert aquatic.clean == False

    def test_get_health_check(self, bushland, aviary, vivarium, farmyard, savannah, aquatic, vet):
        assert bushland.health_check == False
        assert aviary.health_check == False
        assert vivarium.health_check == False
        assert farmyard.health_check == False
        assert savannah.health_check == False
        assert aquatic.health_check == False
        vet.clock_in()
        aquatic.check_health(vet)
        assert aquatic.health_check == True

    # Tests for staff classes

    def test_get_staff_name(self, zookeeper, vet):
        assert zookeeper.staff_name == "Bill"
        assert vet.staff_name == "Ben"

    def test_get_staff_id(self, zookeeper, vet):
        assert zookeeper.staff_id == 4
        assert zookeeper.staff_id != "4"
        assert vet.staff_id == 5
        assert vet.staff_id != "five"

    def test_id_increment(self, zookeeper, vet):
        assert vet.staff_id == zookeeper.staff_id + 1

    def test_get_attendance(self, zookeeper, vet):
        assert zookeeper.working == False
        assert vet.working == False
        zookeeper.clock_in()
        assert zookeeper.working == True

    def test_clock_in(self, zookeeper, vet):
        assert zookeeper.working == False
        zookeeper.clock_in()
        assert zookeeper.working == True
        assert vet.working == False
        vet.clock_in()
        assert vet.working == True



