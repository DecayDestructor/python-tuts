import sys
import random

print("")


playerChoice = input("Enter...\n1. Rock \n2.Paper \n3.Scissors\n")

player = int(playerChoice)

if player < 1 | player > 3:
    sys.exit("Enter a valid choice")

computerChoice = random.choice("123")

computer = int(computerChoice)

print(
    "\nYou chose : " + playerChoice + "\nComputer choice is : " + computerChoice + "\n"
)

if player == 1 and computer == 3:
    print("Player wins!")

elif player == 2 and computer == 1:
    print("Player wins!")

elif player == 3 and computer == 2:
    print("Player wins!")

else:
    print("Computer wins!")
