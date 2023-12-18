# Ineritance tests

import sys

import pytest

SCOPE = "session"

sys.path.append("../")
from inheritance import CHtruck
from inheritance import UStruck
from inheritance import Truck


@pytest.fixture
def class_obj_CHtruck():
    return CHtruck("Saurer", 90, str())


@pytest.fixture
def class_obj_Truck():
    return Truck("Generic", 120, "6")


def test_inheritance_is_CHtruck(class_obj_CHtruck):
    assert type(class_obj_CHtruck) is CHtruck


def test_inheritance_is_not_truck(class_obj_CHtruck):
    assert type(class_obj_CHtruck) is not UStruck


def test_model_truck(class_obj_Truck):
    assert class_obj_Truck.model == "Generic"
