class Gratitudes:
    def __init__(self):
        self.gratitudes = [] # creates an empty list of gratitudes

    def add(self, gratitude): # adds one item to the list
        self.gratitudes.append(gratitude)

    def format(self): # returns a string 
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
