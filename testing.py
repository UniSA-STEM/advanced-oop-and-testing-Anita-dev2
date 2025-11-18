"""
File: testing.py
Description: This file holds test modules
Author: Anita Maratheftis
ID: 110467133
Username: maray160
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from animal import animal
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
    test_staff = Zookeeper("Bill")

def test_get_name(animal_fixture):
    assert animal_fixture.animal_name == "Caramello"


def test_get_capacity(enclosure_fixture):
    assert enclosure_fixture.capacity == 6