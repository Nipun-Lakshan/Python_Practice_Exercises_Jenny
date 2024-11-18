# Python Project 01
print()
import random

print("Rock - Paper - Scissors: A Classic Game of Strategy and Luck")
print("============================================================")
print("============================================================")
print()
print("Introduction")
print("============")
print()
print(
    "01. Rock-Paper-Scissors is a simple hand-gesture game played by two people."
)
print(
    "02. Player simultaneously forms one of three shapes: rock, paper, scissors."
)
print()
print("Rules")
print("=====")
print()
print("01. Rock beats Scissors.")
print("02. Scissor beats Paper.")
print("03. Paper beats Rock.")
print()
print("Symbols in Numeric Form")
print("=======================")
print()
print("# 0 - Rock")
print("# 1 - Paper")
print("# 2 - Scissor")
print()
user_input = input("Enter your choice (0 / 1 / 2) : ")
user_input_length = len(user_input)
if (user_input_length == 1):
    user_input_in_int = int(user_input)
    if (user_input_in_int in (0, 1, 2)):
        computer_input = random.randint(0, 2)
        print("Computer's choice (0 / 1 / 2) : " + str(computer_input))
        print()
        if (computer_input == user_input_in_int):
            print("Result of the Game: Draw")
            print()
        elif (user_input_in_int == 0 and computer_input == 2):
            print("Result of the Game: Won")
            print()
        elif (user_input_in_int == 2 and computer_input == 0):
            print("Result of the Game: Lost")
            print()
        elif (user_input_in_int < computer_input):
            print("Result of the Game: Lost")
            print()
        elif (user_input_in_int > computer_input):
            print("Result of the Game: Won")
            print()
        print("Thank you... Come again!")
        print("========================")
    else:
        print()
        print("Invalid Input. Please try again!")
        print("================================")
else:
    print()
    print("Invalid Input. Please try again!")
    print("================================")
