# Coding Exercise 11
print()

print("Random Selector for Paying the Food Bill")
print("========================================")
print()
text = input("Enter everyone's names separated by a comma and a space :- ")
list_1 = text.split(", ")
import random

a = random.randint(0, (len(list_1) - 1))
print("The person who will pay the food bill now               : - " +
      list_1[a])
