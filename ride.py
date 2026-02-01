print("Select a ride:")
print("1. Bike")
print("2. car")

choice = int(input("Enter your choice ( 1 or 2):"))

if (choice == 1):
    print("What type of bike?")
    print("\n1. Scooty")
    print("\n2. Scooter")

    choice2 = int(input("Enter your choice:"))

    if (choice2 == '1'):
        print("You have selected Scooty.")
    
    else:
        print("You have selected Scooter.")

elif (choice == 2):
    print("What type of car?")
    print("\n1. Sedan")
    print("\n2. XUV")

    choice3 = int(input("Enter your choice:"))

    if (choice3 == '1'):
        print("You have selected Sedan.")
    
    else:
        print("You have selected XUV.")

else:
    print("Wrong choice!")