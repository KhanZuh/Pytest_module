from lib.password_checker import PasswordChecker
import pytest

# Test 1: Password with exactly 8 characters returns True
def test_password_exactly_8_chars_returns_true():
    checker = PasswordChecker()
    assert checker.check("password") == True

# Test 2: Password longer than 8 characters returns True
def test_password_longer_than_8_chars_returns_true():
    checker = PasswordChecker()
    assert checker.check("longpassword") == True

# Test 3: Password shorter than 8 characters raises an exception
# - Check that the exception message is "Invalid password, must be 8+ characters."
def test_password_shorter_than_8_chars_raises_error():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("short")
    assert str(e.value) == "Invalid password, must be 8+ characters."