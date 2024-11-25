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

#############Start Here
