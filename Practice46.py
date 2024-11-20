# Python Sets
print()

# Example 01
set1 = {10, 56, 89, 90, "Jenny", True}
print("Set 01 = " + str(set1))  # Set 01 = {True, 90, 56, 89, 10, 'Jenny'}
set1.add(99)  # add() method
print("Set 01 = " + str(set1))  # Set 01 = {True, 99, 90, 56, 89, 10, 'Jenny'}
print()
set2 = {10, 56, 89, 90, 'Jenny', True, 10, 1}
print("Set 02 = " + str(set2))  # Set 02 = {True, 90, 'Jenny', 56, 89, 10}
print("Set 02 Length: " +
      str(len(set2)))  # Set 02 Length: 6 // Dupliactes will not consider.
set2.remove(10)
print()
print("Set 02 = " + str(set2))  # Set 02 = {True, 'Jenny', 90, 56, 89}
# print(set2.remove(56)) // No Return
set2.discard(56)
print("Set 02 = " + str(set2))  # Set 02 = {True, 90, 89, 'Jenny'}
set2.discard(68)
print("Set 02 = " + str(set2))  # Set 02 = {True, 90, 89, 'Jenny'}
set2.clear()  # Remove all the elements.
print("Set 02 = " + str(set2))  # Set 02 = set()
print()

# Example 02
set1 = {10, True, 'Jenny', 1.11, 1, False, 0}
print("Set 01 = " + str(set1))  # Set 01 = {False, True, 1.11, 'Jenny', 10}
random_poped_element = set1.pop()  # No arguments
print("Set 01 = " + str(set1))  # Set 01 = {True, 1.11, 'Jenny', 10}
print("Random Popped Element : " +
      str(random_poped_element))  # Random Popped Element : False
print()

# Example 03
set3 = {10, True, 'Jenny', 1.11, 1, False, 0}
print("Set 03 = " + str(set3))  # Set 03 = {False, True, 1.11, 'Jenny', 10}
# set3.add(13, 14, 15) // add() method only takes one argument.
# set3.add([48, 44, 43]) // cannot add list for set.
set3.update([44, 45, 48])
print("Set 03 = " +
      str(set3))  # Set 03 = {False, True, 1.11, 45, 48, 10, 44, 'Jenny'}
