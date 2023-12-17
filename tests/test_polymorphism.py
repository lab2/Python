# Polymorphism tests

import sys

sys.path.append("../")
from polymorphism import Vehicle


def test_polymorphism():
    vehicle = Vehicle("Parent brand", "Parent model")
    assert Vehicle("brand", "model").move() == "Move!"
