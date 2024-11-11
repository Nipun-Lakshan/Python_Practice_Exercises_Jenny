# F - String Formatting Exercises
print()
name = "Krishna"  # String
age = 30  # Integer
height = 1.6  # Floating Point Number
# print("My name is " + name + ". My age is " + age + ". My height is " + height + ".") // All the variables should be in String data type.
print(f"My name is {name}. \nMy age is {age}. \nMy height is {height} meters."
      )  # Using f
print()
print(F"My name is {name}. \nMy age is {age}. \nMy height is {height} meters."
      )  # Using F
print()
print(
    F"My name is {name}. \nMy age is {age} years old. \nMy height is {height} meters."
)  # Strings and Variables
print()
print(F"Krishna's father's age is {age * 2} years old."
      )  # Strings and Expressions
name = "Jenny"
age = 31
height = 1.5
print()
print(f"{2 * age}")  # 62
print(f"My father's age is {2 * age}.")
