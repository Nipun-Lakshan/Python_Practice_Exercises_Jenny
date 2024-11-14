# Sample Code for Lists in Python with Methods
print()

# Case 01: Using append() method
list_1 = [1, 5, 7, -9, 12, 25]
print("list_1 = " + str(list_1))  # list_1 = [1, 5, 7, -9, 12, 25]
list_1.append(-12)
print(list_1)  # [1, 5, 7, -9, 12, 25, -12]
print()

# Case 02: Using extend() method
list_2 = [1, 0, 5, -9, 78, 20, 5]
print("list_2 = " + str(list_2))  # list_2 = [1, 0, 5, -9, 78, 20, 5]
list_2.extend([44, 444])
print(list_2)  # [1, 0, 5, -9, 78, 20, 5, 44, 444]
print()

# Case 03: Using insert()
list_3 = [1, 0, 15, -9, 78, 20, 15]
print("list_3 = " + str(list_3))  # list_3 = [1, 0, 15, -9, 78, 20, 15]
list_3.insert(3, 88)
print(list_3)  # [1, 0, 15, 88, -9, 78, 20, 15]
print()

# Case 04: Using remove()
list_4 = [1, 10, 15, -9, 78, 20, 15]
print("list_4 = " + str(list_4))  # list_4 = [1, 10, 15, -9, 78, 20, 15]
list_4.remove(1)
print(list_4)  # [10, 15, -9, 78, 20, 15]
print()

# Case 05: Using pop()
list_5 = [1, 10, 15, -9, 78, 20, 15, -20]
print("list_5 = " + str(list_5))  # list_5 = [1, 10, 15, -9, 78, 20, 15, -20]
print(list_5.pop(-1))  # -20
print(list_5)  # [1, 10, 15, -9, 78, 20, 15]
print(list_5.pop(2))  # 15
print(list_5)  # [1, 10, -9, 78, 20, 15]
print()

# Case 06: Using clear()
list_6 = [1, 2, 3, 4, 5]
print("list_6 = " + str(list_6))  # list_6 = [1, 2, 3, 4, 5]
list_6.clear()
print(list_6)  # []
print()

# Case 07: Using index()
list_7 = [1, 2, 3, 4, 5, 8]
print("list_7 = " + str(list_7))  # list_7 = [1, 2, 3, 4, 5, 8]
print(list_7.index(4))  # 3
a = list_7.index(8)
print(a)  # 5
print()

# Case 08: Using count()
list_8 = [10, 12, 12, 89, 63, 42]
print("list_8 = " + str(list_8))  # [10, 12, 12, 89, 63, 42]
print(list_8.count(12))  # 2
mix_list = [10.10, True, True, 12, 12, 12, "Jenny"]
print(mix_list.count(True))  # 2
print(mix_list.count(12))  # 3
print()

# Case 09: Using sort()
list_9 = [12, 15, 8, -20, 14, 12.5]
print(list_9)  # [12, 15, 8, -20, 14, 12.5]
list_9.sort()
print(list_9)  # [-20, 8, 12, 12.5, 14, 15]
print()

# Case 10: Using reverse()
list_10 = [1, 0, -5, 41, 69, 12.5, True, "Jenny"]
print(list_10)  # [1, 0, -5, 41, 69, 12.5, True, 'Jenny']
list_10.reverse()
print(list_10)  # ['Jenny', True, 12.5, 69, 41, -5, 0, 1]
print()

# Case 11: Using Copy()
list_11 = [12, 56, -89, 63, 45]
print(list_11)  # [12, 56, -89, 63, 45]
list_12 = list_11.copy()
print(list_12)  # [12, 56, -89, 63, 45]
print()

# Case 12: del statement
list_13 = [-5, 8, 3, 0, 10, 65, 789, 632]
print(list_13)  # [-5, 8, 3, 0, 10, 65, 789, 632]
del list_13[0]  # Delete an element by index
print(list_13)  # [8, 3, 0, 10, 65, 789, 632]
del list_13[0:1]  # Delete a slice of the list
print(list_13)  # [3, 0, 10, 65, 789, 632]
del list_13[0:4:2]  # Delete by step
print(list_13)  # [0, 65, 789, 632]
del list_13  # After this row, list_13 will erased from the memory
list_13 = [-5, 8, 3, 0, 10, 65, 789, 632]  # Recalling the list
del list_13[:]  # Delete all elements
print(list_13)  # []
print()

# Case 13: Using print()
list_14 = [12, 15, True, "Jenny", 10.123569]
print(list_14)  # [12, 15, True, "Jenny", 10.123569]
print(list_14[1])  # 15
print(list_14[0:4])  # [12, 15, True, 'Jenny']
list_14[2] = False
print(list_14)  # [12, 15, False, 'Jenny', 10.123569]
list_14[0:4] = [15, 12, "Jenny", False, 10.12]
print(list_14)  # [15, 12, 'Jenny', False, 10.12, 10.123569]

# Case 14: Using min(), max() and len()
list_15 = [1, 5, 9, 5, 3, 0]
print(max(list_15))  # 9
print(min(list_15))  # 0
print(len(list_15))  # 6
print()
