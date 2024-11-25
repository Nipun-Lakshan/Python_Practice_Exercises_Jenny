# Python Sets
print()

# Example 01

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
print(set1.isdisjoint(set2))  # False
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jiya', 'Aakash'}
print(set1.isdisjoint(set2))  # True
print()

# Example 02

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jiya', 'Aakash'}
print(set1.isdisjoint('Mohan', ))  # True
print(set1.isdisjoint(['Mohan']))  # True
print()

# Example 03

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jiya', 'Aakash'}

print(set1.issubset(['Mohan', 'Shiva', 'Jenny'])) # False
print(set1.issubset(('Shiva', 'Jenny', 'Ram', 'Shyam'))) # True
print(set1.issubset(set2)) # False
print(set1 <= set2) # False
print(set1 <= set1) # True
print()

# Example 04

set1 = {'Ram', 'Shyam', 'Jenny', 'Jiya', 'Aakash'}
set2 = {'Jiya', 'Aakash'}
print(set2 <= set1) # True
print(set1.issuperset(set2)) # True
print(set1 >= set2) # True
print(set2.issuperset(set1)) # False
print(set2 >= set1) # False
print(set1.issuperset(set1)) # True
print(set1 >= set2) # True
set2.clear()
print(set2) # set()
del set2
# print(set2) // Not exists a set2 after del statement
print()


