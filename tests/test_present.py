from lib.present import *
import pytest

# Test: wrapping a present stores the content# - Should store the contents and allow unwrap() to return it
def test_wrap_stores_content():
    present = Present()
    present.wrap("book")
    assert present.unwrap() == "book"
# Test: wrapping twice raises an error
def test_wrap_twice_raises_error():
    present = Present()
    present.wrap("toy")
    with pytest.raises(Exception) as e: # “Hey, we expect an error to happen if we try something wrong next.”
        present.wrap("game") # We try to put another thing — a game — inside and wrap it again. But the box is already wrapped, so this should cause an error.
    assert str(e.value) == "A contents has already been wrapped." # Finally, we check that the error message we got is exactly this: "A contents has already been wrapped."

# Test: unwrap returns the content that was wrapped
def test_unwrap_returns_wrapped_content():
    present = Present()
    present.wrap("socks")
    result = present.unwrap()
    assert result == "socks"

# Test: unwrap before wrapping raises an error
def test_unwrap_before_wrap_raises_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."


# Understanding pytest imports:

# with pytest.raises(Exception) as e: --> This line says, "I expect the code inside this block to cause an error (an Exception)."
# How it works:
# pytest.raises(Exception) tells the test, “Watch for an error of type Exception inside this block.”
# If no error happens, the test fails (because you expected an error).
# If an error does happen, pytest saves it in the variable e so you can check it later.

# assert str(e.value) == "A contents has already been wrapped."
# What it means: After catching the error in e, this line checks that the error message is exactly "A contents has already been wrapped."

