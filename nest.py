str = input("Enter a word:")

char = input("Enter a character:")
i = 0
count = 0

while (i < len(str)):

    if(str[i] == char):
        count = count + 1
    i = i + 1

print("The Total Number of Times ", char, "has Occured is: ", count)