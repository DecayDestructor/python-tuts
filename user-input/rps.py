import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(1))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)


print("")


playerChoice = input("Enter...\n1.Rock \n2.Paper \n3.Scissors\n")

player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit("Enter a valid choice")

computerChoice = random.choice("123")

computer = int(computerChoice)

print(
    "\nYou chose : "
    + str(RPS(player)).replace("RPS.", "")
    + "\nComputer choice is : "
    + str(RPS(computer)).replace("RPS.", "")
    + "\n"
)

if player == 1 and computer == 3:
    print("Player wins!")

elif player == 2 and computer == 1:
    print("Player wins!")

elif player == 3 and computer == 2:
    print("Player wins!")

elif player == computer:
    print("It's a tie!")

else:
    print("Computer wins!")
