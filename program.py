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
from enclosure import Bushland
from staff import Zookeeper

@pytest.fixture
def animal_fixture():
    return Mammal("Caramello", "koala", 5, "herbivore")

@pytest.fixture
def enclosure_fixture():
    return Bushland()

@pytest.fixture
def staff_fixture():
    return Zookeeper("Bill")

def test_get_name(animal_fixture):
    assert animal_fixture.animal_name == "Caramello"

def test_get_age(animal_fixture):
    assert animal_fixture.age == 5

def test_get_dietary_needs(animal_fixture):
    assert animal_fixture.diet == "Herbivore"

def test_get_species(animal_fixture):
    assert animal_fixture.species == "koala"

def test_get_health(animal_fixture):
    assert animal_fixture.get_health() == "Healthy"

def test_health_status(animal_fixture):
    assert animal_fixture.health_status() == "Healthy" or "Injured" or "Sick" or "Behaviourally Challenged"

def test_str(animal_fixture):
    assert animal_fixture.__str__() == "Meet Caramello! Caramello is a koala, and is 5 years old. Caramello is a Herbivore.\nTo learn more about Caramello, ask one of our friendly Zookeepers!\n"

def test_get_capacity(enclosure_fixture):
    assert enclosure_fixture.capacity == 6

