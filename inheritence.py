class dad:

    def __init__(self, eyes, agressive):

        self.eyes = eyes
        self.agressive = agressive

    def display (self):
            print("Your eye colour is: ", self.eyes)
            print("You are agressive: ", self.agressive)

class son(dad):
    def __init__(self, name, age, eyes, agressive):
        self.name = name
        self.age = age

        dad.__init__(self, eyes, agressive)

obj = son('Penguin', 8, 'Blue', True)

obj.display()