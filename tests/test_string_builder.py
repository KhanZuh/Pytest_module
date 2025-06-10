from lib.string_builder import *

# Test 1: Test inital state of new StringBuilder instance
def test_initial_state_of_string_builder(): 
# Create a new StringBuilder 
    string_builder = StringBuilder()
# check that the output() returns an empty string
    assert string_builder.output() == ""
# check that size() returns 0
    assert string_builder.size() == 0

# Test 2: Test adding a single string
def test_add_multiple_strings():
# - Create a new StringBuilder
    string_builder = StringBuilder()
# - Call add("hello")
    string_builder.add("hello")
# - Check that output() returns "hello"
    assert string_builder.output() == "hello"
# - Check that size() returns 5
    assert string_builder.size() == 5   


# Test 3: Test adding multiple strings
def test_add_multiple_strings():
# - Create a new StringBuilder
    string_builder = StringBuilder()
# - Call add("hello"), then add(" world")
    string_builder.add("hello")
    string_builder.add(" world")
# - Check that output() returns "hello world"
    assert string_builder.output() == "hello world"
# - Check that size() returns 11
    assert string_builder.size() == 11



# Test 4: Test adding an empty string
def test_add_empty_string():
# - Create a new StringBuilder
    string_builder = StringBuilder()
# - Call add("")
    string_builder.add("")
# - Check that output() is still an empty string
    assert string_builder.output() == ""
# - Check that size() is still 0
    assert string_builder.size() == 0


# Edge cases
# Edge case Test 5: Test behavior when non-string is added
def test_add_non_string_raises_type_error():
    string_builder = StringBuilder()  

    # Try to add a non-string value directly
    try:
        string_builder.add(123)  
    except TypeError:
        # If TypeError is raised, the test passes, so we return early
        return

    # If no error was raised, fail the test explicitly with a message
    assert False, "TypeError not raised"



