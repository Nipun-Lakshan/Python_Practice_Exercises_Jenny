# Coding Exercise 11
print()

# Head and Tails
import random

a = random.randint(0, 1)  # Generate a number either 0 or 1.
print("Welcome to Virtual Head or Tail Game!")
print("=====================================")
print()
input = input("Guess whether it will be heads or tails (H/T):- ")
user_input = -1
if (input in ("H", "h")):
    user_input = 1
elif (input in ("T", "t")):
    user_input = 0
else:
    print("Invalid Input! Please try again!")
    print("=================================================")
if (user_input == a and a == 1 and input in ("H", "h", "T", "t")):
    print("Result received from the virtual coin        :- Head")
    print("You won!")
    print("Thank you for participating!")
    print("====================================================")
elif (user_input == a and a == 0 and input in ("H", "h", "T", "t")):
    print("Result received from the virtual coin        :- Tail")
    print("You won!")
    print("Thank you for participating!")
    print("====================================================")
elif (user_input != a and a == 0 and input in ("H", "h", "T", "t")):
    print("Result received from the virtual coin        :- Tail")
    print("You lost!")
    print("Thank you for participating!")
    print("====================================================")
elif (user_input != a and a == 1 and input in ("H", "h", "T", "t")):
    print("Result received from the virtual coin        :- Head")
    print("You lost!")
    print("Thank you for participating!")
    print("====================================================")
