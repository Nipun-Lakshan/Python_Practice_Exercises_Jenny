# Python Sets
print()

# Example 01
set1 = {10, True, 'Jenny', 1.11}
print("Set 01 = " + str(set1))  # Set 01 = {True, 10, 1.11, 'Jenny'}
set2 = {1, 2, 10, -10, 0, 53}
print("Set 02 = " + str(set2))  # Set 02 = {0, 1, 2, 53, -10, 10}
set3 = {1, 2, 10, -10, 0, 53, 1}
print("Set 03 = " + str(set3))  # Set 03 = {0, 1, 2, 53, -10, 10}

# No Order. Duplicates are not allowed.
# set2[2] = 10 // Indexing is not allowed. Elements are unchangeable.

set4 = {10, True, 'Jenny', 1.11, 1, False, 0}
print("Set 04 = " + str(set4))  # Set 04 = {False, True, 1.11, 'Jenny', 10}
print()

# Example 02
set1 = {10, 56, 89, 90, "Jenny", True}
print("Set 01 = " + str(set1))  # Set 01 = {True, 90, 56, 89, 10, 'Jenny'}
set2 = {10, 56, 89, 90, 'Jenny', True, 10, 1}
print("Set 02 = " + str(set2))  # Set 02 = {True, 'Jenny', 90, 56, 89, 10}
# print(set2[2]) // No Index, No Order
set3 = {}  # Not a empty set. It is an empty dictionary.
print("Set 03 = " + str(set3))  # Set 03 = {}
print()
print("Set 02 Type = " + str(type(set2)))  # Set 02 Type = <class 'set'>
print("Set 03 Type = " + str(type(set3)))  # Set 03 Type = <class 'dict'>
print()
set4 = set()  # Empty Set // Only Method
print("Set 04 = " + str(set4))
print("Set 04 Type = " + str(type(set4)))
# set2[2] = 99 // 'set' object does not support item assignment
