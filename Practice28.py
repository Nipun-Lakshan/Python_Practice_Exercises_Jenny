# All Types of Placeholders in Python % Formatting
print()

# Case 01: String Placeholder
name = "Jenny"
print("%s is a good lecturer." % (name))  # Output: Jenny is a good lecturer.
print()

# Case 02: Integer Placeholder
num1 = 25
num2 = -25
print("%d is a positive number and %d is a negative number." % (num1, num2))
# Output: 25 is a positive number and -25 is a negative number.
print()

# Case 03: Floating - Point Placeholder
num1 = 25.8967
num2 = -12.89635
print("%.4f is a positive number and %.5f is a negative number." %
      (num1, num2))
# 25.8967 is a positive number and -12.89635 is a negative number.
print()

# Case 04: Hexadecimal Placeholder
print("Hexadecimal Number %x is 10 in decimal numbers." % (10))
print("Hexadecimal Number %X is 10 in decimal numbers." % (10))
print()
# Hexadecimal Number a is 10 in decimal numbers.
# Hexadecimal Number A is 10 in decimal numbers.

# Case 05: Octal Placeholder
print("Octal number %o is 64 in decimal numbers." % (64))
print()
# Octal number 100 is 64 in decimal numbers.

# Case 06: Percentage Placeholder
print("Our gross margin percentage for this quarter is %.4f%%." % (4.7856))
print()
# Our gross margin percentage for this quarter is 4.7856%.

# Case 07: Scientific Notification Placeholder
print("%e" % (478.96314452288624865175182458))  # 4.789631e+02
print("%E" % (0.000000047896314452288624865175182458))  # 4.789631E-08
print()

# Case 08: General Format (Round up the number on its own way)
print("%g" % (4.789779755))  # 4.78978
print("%G" % (4.8965))  # 4.8965
print()

# Case 09: Character Placeholder
print("Char A: %c" % (65))  # Char A: A
print("Char A: %c" % ("A"))  # Char A: A
print()

# Case 10: Unsigned Integer
print("%u" % (-25))  # -25
print("%u" % (25))  # 25
