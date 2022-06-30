class Citizen:
    """A Definition of an upstanding Python Citizen"""
    
    greeting = "For the glory of Python!"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return " ".join([self.first_name,self.last_name])