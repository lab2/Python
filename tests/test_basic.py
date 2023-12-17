# Basic tests

import sys

sys.path.append("../")
from hello_world import HelloWorld


def test_assert_equal():
    assert 2 == 2


def test_hello_world():
    assert HelloWorld().greet() == "Hello world!"
