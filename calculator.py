def add(P, Q):
     return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
     return P * Q

def divide(P, Q):
    return P / Q

print("Please select the operation:-")
print("\na. Add")
print("\nb. Subtract")
print("\nc. Multiply")
print("\nd. Divide")

choice = input("Enter choice(a/b/c/d):")

num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))

if choice == "a":
     print(num1 ," + ", num2, " = ", add( num1, num2))

elif choice == "b":
     print(num1 ," - ", num2, " = ", subtract( num1, num2))

elif choice == "c":
     print(num1 ," x ", num2, " = ", multiply( num1, num2))

elif choice == "d":
     print(num1 ," / ", num2, " = ", divide( num1, num2))

else:
     print("Invalid Input!")