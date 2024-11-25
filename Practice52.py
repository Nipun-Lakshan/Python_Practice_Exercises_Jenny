# Python Sets
print()

# Example 01

set1 = {1, 2, 3, 4, 5}
set2 = {4, 10, 7, 8, -10}
print(set1.isdisjoint(set2))  # False, 4 is common for both sets!
print(set1.issubset(set2))  # False
print(set1.isdisjoint([5]))  # False
print()

# Example 02

set1 = {1, 2, 3, 4, 5}
set2 = {4, 10, 7, 8, -10, 1, 2, 3, 5}
print(set1.issubset(set2))  # True
print(set1 <= set2)  # True
print()

# Example 03

set1 = {1, 2, 3, 4, 5}
set2 = {4, 10, 7, 8, -10, 1, 2, 3, 5}
set3 = {1, 2, 3, 4, 5, 8}

print(set1.issubset((1, 5, 3)))  # False
print(set1.issubset({1, 4, 9}))  # False
print(set1 <= set2)  # True
print(set2 <= set1)  # False
print(set1.issuperset(set2))  # False
print(set2.issuperset(set1))  # True
print(set2 >= set1)  # True
print(set1 >= set2)  # False
print()

# Example 04

set1 = {1, 2, 3, 4, 5, 10, 7, 8, -10, 11, 53}
set2 = {4, 10, 7, 8, -10, 1, 2, 3, 4, 5}
set3 = {1, 2, 3, 4, 5, 8}
print(set1.issuperset(set2))  # True
print()
