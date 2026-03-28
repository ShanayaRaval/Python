import random

while True:
    user_act = input("Enter a choice(Rock, Paper or Scissors):")
    poss_act = ["Rock", "Paper", "Scissors" ]

    comp_act = random.choice(poss_act)

    print(f"\nYou chose {user_act} and computer chose {comp_act}.\n")

    if user_act == comp_act:
        print(f"Both players slected {user_act}. It's a tie.")

    elif user_act == 'Rock':
        if comp_act == 'Scissors':
            print("Rock smashes scissors. You win!")
        else:
            print("Paper covers rock. You lose!")

    elif user_act == 'Paper':
        if comp_act == 'Rock':
            print(" You win!")
        else:
            print(" You lose!")

    elif user_act == 'Scissors':
        if comp_act == 'Paper':
            print(" You win!")
        else:
            print(" You lose!")

    play_again = input("Do you want to play again?(y/n):")
    if play_again != 'y':
        break