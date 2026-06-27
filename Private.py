class MyClass:

    __privateVar = 27;

    def __privMeth(self):
        print("I'm inside class MyClass.")

    def Hello(self):
        print("Private variable value: ", MyClass.__privateVar)

foo = MyClass()
foo.Hello()
__privMeth()