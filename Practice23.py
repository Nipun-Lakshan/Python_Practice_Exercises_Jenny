# String Formatting Methods in Python
print()
# String Manipulation with Type Casting in Python
name = "Krishna"
age = 30
height = 1.67
print("My name is " + name + ". \nMy age is " + str(age) +
      ". \nMy height is " + str(height) + " meters.")
# My name is Krishna.
# My age is 30.
# My height is 1.67 meters.

# String Formatting Using Commas (,)
print()
name = "Krishna"
age = 30
height = 1.67
print("My name is", name, "\b. \nMy age is", age, "\b. \nMy height is", height,
      "meters.")
# My name is Krishna.
# My age is 30.
# My height is 1.67 meters.

# String Formatting Using Percentage (%)
print()
name = "Krishna"
age = 30
height = 1.67
print("My name is %s. \nMy age is %d. \nMy height is %.2f meters." %
      (name, age, height))
# My name is Krishna.
# My age is 30.
# My height is 1.67.

# String Formatting Using .format().
print()
name = "Krishna"
age = 30
height = 1.67
print("My name is {}. \nMy age is {}. \nMy height is {} meters.".format(
    name, age, height))
# My name is Krishna.
# My age is 30.
# My height is 1.67 meters.

# String Formatting F - Strings.
print()
name = "Krishna"
age = 30
height = 1.67
print(f"My name is {name}. \nMy age is {age}. \nMy height is {height} meters.")
print()
print(F"My name is {name}. \nMy age is {age}. \nMy height is {height} meters.")
# My name is Krishna.
# My age is 30.
# My height is 1.67 meters.

# My name is Krishna.
# My age is 30.
# My height is 1.67 meters.
