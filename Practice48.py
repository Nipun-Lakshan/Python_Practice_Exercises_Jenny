# Python Sets
print()

# Example 01
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set1.update(set2)
print(set1)  # {'Shyam', 'Jenny', 'Ram', 'Jiya', 'Aakash'}
print(set2)  # {'Jiya', 'Aakash', 'Jenny'}
print()

# Example 02
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set2.update(set1)
print(set2)  # {'Jenny', 'Aakash', 'Shyam', 'Ram', 'Jiya'}
print(set1)  # {'Jenny', 'Ram', 'Shyam'}
print()

# Example 03
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set1.update(['jenny', 'Mohan'])
print(set1)  # {'Shyam', 'Jenny', 'jenny', 'Ram', 'Mohan'}
print(set2)  # {'Jenny', 'Aakash', 'Jiya'}
print()

# Example 04
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set1.update(['Jenny', 'Mohan'])
print(set1)  # {'Jenny', 'Shyam', 'Mohan', 'Ram'}
print(set2)  # {'Jenny', 'Aakash', 'Jiya'}
print()

# Example 05
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set1 |= set2
print(set1)  # {'Shyam', 'Ram', 'Jiya', 'Jenny', 'Aakash'}
print(set2)  # {'Jenny', 'Aakash', 'Jiya'}
print()

# Example 06
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

print(set1 | set2 | set3)
print(set1.union(set2, set3))
print()
