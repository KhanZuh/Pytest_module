from lib.greet import *

def test_greet_returns_hello_with_name():
    result = greet("Zuhair")
    assert result == "Hello, Zuhair!"