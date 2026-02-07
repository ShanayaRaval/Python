str = input("Please enter any String of your choice:")

str2 = ('')

for i in str:
    str2 = i + str2
    
print("Original String is : ", str)
print("Reversed String is : ", str2)