class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)

    def output(self):
        return self.str

# Breaking down this function
# 1. What does this function want?
#  This class builds a string by adding pieces to it, can tell me the total size, and can give me the full string.

# 2. What do i give it?
# # I create an instance with no arguments.
# I call add() with strings to add to the internal string.

# 3. What do I expect back?
# # output() returns the combined string.
# size() returns the length of the combined string.

# 4. What if I give it something weird?
# # What if I add an empty string? output() should stay the same, size() unchanged.
# What if I add a non-string like an int? Should it raise an error? 

# 5. What if I do nothing?
# If I never call add(), output() returns "" (empty string) and size() returns 0.

