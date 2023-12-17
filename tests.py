# Simple tests

from helloworld import HelloWorld

def test_assert_equal():
    assert 2 == 2

def test_hello_world():
    assert HelloWorld().greet() == "Hello world!"