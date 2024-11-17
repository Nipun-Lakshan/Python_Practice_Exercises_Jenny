# Index Error in Python
print()

names = [
    "Jenny",
    "Jiya",
    "Payal",
]  # Create a List, Index start from 0.
a = names[1]  # Access an element from sequencea nd stored it in variable.
print(a)  # Jiya
# a = names[3] // IndexError: list index out of range
print()

length = len(names)  # Finding the length of the list.
print("Length of the List: " + str(length))  # Length of the List: 3
print()

a = names[length - 1]
print(a)  # Last Element of the Sequence.
a = names[-1]
print(a)  # First Element from the right of the Sequence.
a = names[-2]
print(a)  # Second Element from the right of the Sequence.
a = names[-3]
print(a)  # Third Element from the right of the Sequence.
# a = names[-4] // IndexError: list index out of range
print()

names = [
    "Jenny",
    "Jiya",
    "Payal",
]
print(f"Hi! {names[2]}")  # Hi! Payal
# print(f"Hi! {names[3]}") // IndexError: list index out of range
print()

names = ["Jenny", "Jiya", "Payal", "Aakash", "Ankur", "Ankush", "Pradeep"]
length = len(names)
# print(f"Hi! {names[length]}") // IndexError: list index out of range
print(f"Hi! {names[length - 1]}")  # Hi! Pradeep
print(f"Hi! {names[-7]}")  # Hi! Jenny
