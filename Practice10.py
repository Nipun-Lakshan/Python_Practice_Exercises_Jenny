# Exercise 15
print()
print(len("Jenny Khatri"))
print(len("12345"))
# print(len(12345)) // len() will only accept a string and it will not accept a int
print(len(str(12345)))  # len() will accept the int conversion as a string

print()
length = len("Jenny Kharti")
print(length)
print(type(length))
# print("Your name has " + length + " Characters.") // Length is an int and it will not concatenate with strings.
print("Your name has " + str(length) + " Characters.")  # Length is now an int and it will concatenate with strings.
a = str(length)
print(type(a))

print()
new_length = str(length)
print(type(new_length))
print(type(length))

'''
Type Conversion
===============

int()
float()
str()

'''

print()
print(10 + 10) # 20
print("10" + "10") # 1010
print(int("10") + int("10")) # 20
# print(10 + "10") // Error due to concatenation of String and Integer
print(10 + int("10")) # 20
print(10 + float("10")) # Implicit Conversion to Float when opearting opeartion between int and float // 20.0

print()
name = "Jenny"
# print(10 + int(name)) Error due to concatenation of String and Int
name = "123"
print(10 + int(name)) # 123 + 10 = 133