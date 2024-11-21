# Python Sets
print()

# Example 01
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 10, 11}
print(set1
      | set2)  # Union of set1 and set2   // Output: {1, 2, 3, 4, 5, 6, 10, 11}
print(set1 & set2)  # Intersection of two sets // Output: {4, 5}
print(set1 - set2)  # Set Difference           // Output: {1, 2, 3}
print(set1 ^ set2)  # Symmetric Difference     // Output: {1, 2, 3, 6, 10, 11}
print()

# Example 02
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}
print(set1.union(set2))  # {'Jiya', 'Shyam', 'Aakash', 'Jenny', 'Ram'}
print(set2.union(set1))  # {'Shyam', 'Jenny', 'Jiya', 'Aakash', 'Ram'}
print(set1 | set2)  # {'Aakash', 'Ram', 'Jiya', 'Shyam', 'Jenny'}
print(set2 | set1)  # {'Ram', 'Jenny', 'Jiya', 'Shyam', 'Aakash'}
print(set1.union(
    set2,
    set3))  # {'Pradeep', 'Shyam', 'Jiya', 'Ram', 'Ankur', 'Aakash', 'Jenny'}
print(
    set1 | set2
    | set3)  # {'Jiya', 'Shyam', 'Aakash', 'Jenny', 'Pradeep', 'Ankur', 'Ram'}
print(set1.union(['Mohan', 'Jenny']))  # {'Mohan', 'Shyam', 'Ram', 'Jenny'}
print(set2.union(('Mohan', 'Jenny')))  # {'Jenny', 'Aakash', 'Mohan', 'Jiya'}
# print(set1 | ('Mohan', 'Jenny')) # Can't work different types with operator
# print(set1 | ['Mohan', 'Jenny']) # Can't work different types with operator
print(set1 | {'Mohan', 'Jenny'})  # {'Ram', 'Mohan', 'Jenny', 'Shyam'}
