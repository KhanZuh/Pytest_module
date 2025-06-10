from lib.counter import *

# 1. Define a test function to check initial count
#  - create instance of the counter 
#  assert that report() returns "COunted to 0 so far"


# 2. Define a test function to check adding a positive number
# - Create an instance of Counter
# - Call add() with a positive number (e.g., 5)
# - Assert that report() returns "Counted to 5 so far."
def test_counter_starts_at_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."


# 3. Define a test function to check adding a positive number
# - Create an instance of Counter
# - Call add() with a positive number (e.g., 5)
# - Assert that report() returns "Counted to 5 so far."
def test_counter_adds_number():
    counter = Counter()
    counter.add(5)
    result =  counter.report()
    assert result == "Counted to 5 so far."

# 4: Try adding multiple numbers
# - Add more than one number (e.g., 3 and then 7)
# - Check that the final report shows the total (should be 10)
def test_counter_adds_multiple_numbers():
    counter = Counter()
    counter.add(3)
    counter.add(7)
    result = counter.report()
    assert result == "Counted to 10 so far."

# Edge Case : Add a negative number
def test_counter_adds_negative_number():
    counter = Counter()
    counter.add(-5)
    result = counter.report()
    assert result == "Counted to -5 so far."