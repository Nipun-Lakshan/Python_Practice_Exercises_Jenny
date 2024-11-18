# Tuples in Python
print()

# Example 01
tuple1 = (10, 1, -10, 15, 20)
tuple2 = ('Jenny', 'Ram', 'Shyam')
tuple4 = (10)
tuple5 = (10, )
print(type(tuple4))  # <class 'int'>
print(type(tuple5))  # <class 'tuple'>
print()

# Example 02
tuple7 = (12, 6, -8, 'Jenny', True)
print(tuple7)  # (12, 6, -8, 'Jenny', True)
print(tuple7[-2])  # Jenny
# print(tuple1[-6]) // IndexError: tuple index out of range
# print(tuple6[7]) // IndexError: tuple index out of range
print(type(tuple7))  # <class 'tuple'>
# tuple7[0] = 13 // TypeError: 'tuple' object does not support item assignment
print()

# Example 03
tuple8 = (12, 6, -8, 'Jenny', True, 12, 6)  # Duplicates are allowed!
print(tuple8)  # (12, 6, -8, 'Jenny', True, 12, 6)
print(tuple8[1:])  # (6, -8, 'Jenny', True, 12, 6)
print(tuple8[1:4])  # (6, -8, 'Jenny')
print(tuple8[:4])  # (12, 6, -8, 'Jenny')
print(tuple8[::2])  # (12, -8, True, 6)
print(len(tuple8))  # 7
print()

# Example 04
tuple9 = (45, 67, 90)
tuple10 = (12, 6, -8, 'Jenny', True, 12, 6)
tuple11 = (tuple9, tuple10)  # Nested Tuple
print(tuple11)  # ((45, 67, 90), (12, 6, -8, 'Jenny', True, 12, 6))
list1 = list(tuple9)
list2 = list(tuple10)
list3 = [list1, list2]  # Nested List
print(list3)  # [[45, 67, 90], [12, 6, -8, 'Jenny', True, 12, 6]]
print(tuple11[1])  # (12, 6, -8, 'Jenny', True, 12, 6)
print(len(tuple11))  # 2
print()

# Example 05
tuple_1 = (12, 6, -8, 'Jenny', True, 12, 6)
tuple_2 = (45, 67, 90)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)  # (12, 6, -8, 'Jenny', True, 12, 6, 45, 67, 90)
print(min(tuple_2))  # 45
print(max(tuple_2))  # 90
print(tuple_1.count(12))  # 2
print(tuple_1.index(12))  # 0
print()

# Example 06
list_01 = [1, 2, 3, 4, 5]
print(tuple(list_01))  # (1, 2, 3, 4, 5)
tuple_4 = (10, ) * 5
string = "5" * 4
print(tuple_4)  # (10, 10, 10, 10, 10)
print(string)  # 5555
