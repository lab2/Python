# Simple tests

import sys
sys.path.insert(0, "../")
from hello_world import HelloWorld

def test_assert_equal():
    assert 2 == 2

def test_hello_world():
    assert HelloWorld().greet() == "Hello world!"