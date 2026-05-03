class Employee:

    def __init__(self):
        print("Employee created!")

    def __del__(self):
        print("Destructor called!")

def create_ob():
    print("Making object...")
    obj = Employee()
    print("Function end.")
    return obj

print("Calling Create Object function... ")

obj = create_ob()

print("Program end.")