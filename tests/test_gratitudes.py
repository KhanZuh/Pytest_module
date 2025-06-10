from lib.gratitudes import *

# test inital state
# - When a Gratitudes object is created, the gratitudes list should be empty
def test_initial_gratitudes_is_empty():
        gratitude = Gratitudes()
        assert gratitude.gratitudes == []


# Test 2: Adding one gratitude
# - After calling add("sunshine"), the list should contain "sunshine"
def test_add_single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("sunshine")
    assert gratitude.gratitudes == ["sunshine"]



# Test 3: Adding multiple gratitudes
# - After calling add("sunshine") and add("coffee"), the list should contain both items




# Test 4: Formatting output with one gratitude
# - After adding "sunshine", format() should return "Be grateful for: sunshine"

# Test 5: Formatting output with multiple gratitudes
# - After adding "sunshine" and "coffee", format() should return "Be grateful for: sunshine, coffee"
