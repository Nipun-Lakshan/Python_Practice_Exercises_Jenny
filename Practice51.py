# Python Sets
print()

# Example 01
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

print(set1.symmetric_difference(set2))  # {'Ram', 'Jiya', 'Aakash', 'Shyam'}
# print(set1.symmetric_difference(set2, set3)) // Only One Argument
print(set1.symmetric_difference(('Jenny', )))  # {'Ram', 'Shyam'}
print(set1 ^ set2)  # {'Jiya', 'Ram', 'Shyam', 'Aakash'}
print(set1 ^ set2 ^ set3)  # {'Ankur', 'Jiya', 'Aakash', 'Shyam', 'Pradeep'}
print()

# Example 02

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

set2.symmetric_difference_update(set1)
print(set2)  # {'Jiya', 'Ram', 'Shyam', 'Aakash'}
print(set1)  # {'Ram', 'Shyam', 'Jenny'}
print()

# Example 03

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}
set1.symmetric_difference_update(('Mohan', 'Shiva'))
print(set1)  # {'Ram', 'Shyam', 'Mohan', 'Jenny', 'Shiva'}
print(set2)  # {'Aakash', 'Jiya', 'Jenny'}
print()

# Example 03

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

print(set1 ^ set2 ^ set3)  # {'Ankur', 'Pradeep', 'Shyam', 'Aakash', 'Jiya'}
set1 ^= set2
print(set1)  # {'Aakash', 'Ram', 'Shyam', 'Jiya'}
print(set2)  # {'Jenny', 'Aakash', 'Jiya'}
print()
