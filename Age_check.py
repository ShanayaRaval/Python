try:
    age = int(input("Enter your age:"))
    print("Your age is: ", age)

except ValueError:
    print("Error! Please enter any age like 12,14,27.")

