# Python Sets
print()

# Example 01
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

print(set1.intersection(set2))  # {'Jenny'}
print(set1)  # {'Shyam', 'Ram', 'Jenny'}
print(set2)  # {'Aakash', 'Jenny', 'Jiya'}
print(set2.intersection(set1))  # {'Jenny'}
print(set1)  # {'Jenny', 'Ram', 'Shyam'}
print(set2)  # {'Jenny', 'Jiya', 'Aakash'}
print(set1.intersection(set2, set3))  # set()
print(set1)  # {'Ram', 'Shyam', 'Jenny'}
print(set2)  # {'Jenny', 'Aakash', 'Jiya'}
print(set3)  # {'Pradeep', 'Ankur'}
print(set1 & set2)  # {'Jenny'}
print(set1 & set2 & set3)  # set()
print(set1)  # {'Shyam', 'Ram', 'Jenny'}
print(set2)  # {'Jenny', 'Aakash', 'Jiya'}
print(set3)  # {'Ankur', 'Pradeep'}
print(set1 & {"Ram", "Shyam"})  # {'Ram', 'Shyam'}
print(set1 & {'jenny'})  # set()
print()

# Example 02
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

print(set1 & set2)  # {'Jenny'}
print(set2 & set3)  # set()
print(set1 & set2 & set3)  # set()
print(set1.intersection(['Mohan', 'Shiva']))  # set()
set1 &= set2
print(set1)  # {'Jenny'}
print(set2)  # {'Jiya', 'Aakash', 'Jenny'}
print()

# Example 03
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set1.intersection_update(set2)
print(set1)  # {'Jenny'}
print(set2)  # {'Aakash', 'Jiya', 'Jenny'}
print()

# Example 04
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

set2.intersection_update(set1)
print(set1)  # {'Shyam', 'Jenny', 'Ram'}
print(set2)  # {'Jenny'}
print()

# Example 05
set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}
set1.intersection_update(['Ram'])
print(set2) # {'Jiya', 'Aakash', 'Jenny'}
print(set3) # {'Pradeep', 'Ankur'}
set2.intersection_update(('Jenny',))
set3.intersection_update({'Ankur'})
print(set1) # {'Ram'}
print(set2) # {'Jenny'}
print(set3) # {'Ankur'}
print()