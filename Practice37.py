# Random Module in Python
import random

print()

# Case 01: randint()
a = random.randint(1, 3)  # 1 <= x <= 3; X is the random number.
print(a)  # 1, 2 or 3
print()

# Case 02: randrange()
a = random.randrange(1, 3)  # 1 <= x <3; X is the random number.
print(a)  # 1 or 2
print()

# Case 03: random()
a = random.random()  # 0.0 <= x < 1.0; X is the random number.
print(a)
print()

# Case 04: uniform()
a = random.uniform(1, 3)  # 1.0 <= x <= 3.0
print(a)
print()

# Case 05: choice()
l = [2, 5, 90, -5, 89, 12, 56]
a = random.choice(l)  # One of the value of the list
print(a)
print()

# Case 06: Shuffle()
l = [2, 5, 90, -5, 89, 12, 56]
random.shuffle(l)  # No Return
print(l)
