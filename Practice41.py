# Nested Lists in Python Programming
print()

# Example 01
numbers = [1, 10, 15, 20, -10, 15]
mix_list = [1, 10, "Jenny", True]
nested_list = [1, 10, 15, [20, -10, 15], 17, 0]
print("nested_list = " +
      str(nested_list))  # nested_list = [1, 10, 15, [20, -10, 15], 17, 0]
print("Length of the List: " + str(len(nested_list)))  # Length of the List: 6
print("First Element: " + str(nested_list[0]))  # First Element: 1
print("Fourth Element: " +
      str(nested_list[3]))  # Fourth Element: [20, -10, 15]
print("First Element in Inner List: " +
      str(nested_list[3][0]))  # First Element in Inner List: 20
print("Second Element in Inner List: " +
      str(nested_list[3][1]))  # Second Element in Inner List: -10
print()

# Example 02
list_1 = [10, 34, 90, [45, 78, -3], 89]
print(len(list_1))  # 5
print(list_1[4])  # 89
print(list_1[3])  # [45, 78, -3]
print(list_1[3][2])  # -3
print(list_1[-2])  # [45, 78, -3]
print(list_1[len(list_1) - 1])  # 89
print(list_1[len(list_1) - 2])  # [45, 78, -3]
print(list_1[3][0:3])  # [45, 78, -3]
print(list_1[3][0:2])  # [45, 78]
print(list_1[3][::])  # [45, 78, -3]
print(list_1[3][::2])  # [45, -3]
print()

# Example 03
mixed_list = [10, 34, 90, ["Mohan", "Shyam", "Ram"], 89]
print("mixed_list = " + str(mixed_list)
      )  # mixed_list = [10, 34, 90, ['Mohan', 'Shyam', 'Ram'], 89]
print("Is above list valid?: " + "Yes")  # Is above list valid?: Yes
print("Length of the list: " + str(len(mixed_list)))  # Length of the list: 5
print("Last Element of Inner List: " +
      str(mixed_list[3][2]))  # Last Element of Inner List: Ram
