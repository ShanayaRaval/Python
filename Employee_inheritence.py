class person:
    
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
    
    def display(self):
        print(self.name)
        print(self.idnum)

class employee(person):

    def __init__(self, name, idnum, salary, post):
        self.salary = salary
        self.post = post

        person.__init__(self, name, idnum)

a = employee('Rahul', 886012, 200000, 'intern')

a.display()