# Simple tests

import sys
from hello_world import HelloWorld
sys.path.insert(0, "..")

def test_assert_equal():
    assert 2 == 2

def test_hello_world():
    assert HelloWorld().greet() == "Hello world!"