count = 0
num = int(input("Enter a number:"))

while (num > 0):
    num = num // 10
    count = count + 1

print("Total number of digits is: ", count)