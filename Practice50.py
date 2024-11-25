# Python Sets
print()

# Example 01
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

print(set1.difference(set2, set3))  # {'Ram', 'Shyam'}
print(set1 - set2)  # {'Shyam', 'Ram'}
print(set1.difference(('Mohan', 'Shiva')))  # {'Shyam', 'Ram', 'Jenny'}
print(set1.difference(['Mohan', 'Shiva']))  # {'Shyam', 'Ram', 'Jenny'}
print()

# Example 02
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

print(set1.difference(set2, set3))  # {'Shyam'}
print(set1 - set2 - set3)  # {'Shyam'}
# print(set1-('Jenny',)-['Ram'])
print()

# Example 03

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

set1.difference_update(set2)
print(set1)  # {'Ram', 'Shyam'}
print(set2)  # {'Jiya', 'Aakash', 'Jenny'}
print()

# Example 04

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

set2.difference_update(set1)
print(set1)  # {'Jenny', 'Ram', 'Shyam'}
print(set2)  # {'Aakash', 'Jiya'}
print()

# Example 05
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

set1 -= set2
print(set1)  # {'Ram', 'Shyam'}
print(set2)  # {'Aakash', 'Jenny', 'Jiya'}
print()
