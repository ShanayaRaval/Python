class bird:

    def __init__(self):
        print("Bird is ready!")

    def WhoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class penguin(bird):

    def __init__(self):

        super().__init__()
        print("Penguin is ready!")
    
    def WhoIsThis(self):
        print("Penguin")
