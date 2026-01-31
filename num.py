print("Enter a number(numerator):")
num = int(input())
print("Enter a number(denominator):")
numd = int(input())

if num%numd == 0:
    print("\n" + str(num) + " is divisible by " + str(numd))

else:
     print("\n" + str(num) + " is not divisible by " + str(numd))