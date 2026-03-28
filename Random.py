import random
playing = True
num = str(random.randint(0 ,9))

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get ome hero!")

while playing:
    guess = input("Give me best guess! \n")
    if num == guess:
        print("You won!")
        print("The number was ", num)
        break

    else:
        print("Your guess isn't quite right, try again!")
