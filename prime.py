up = int(input("Enter an Upper range:"))
low = int(input("Enter a Lower range:"))

print ("Prime numbers between ", low, "and ", up, "are:")

for num in range(low, up +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)