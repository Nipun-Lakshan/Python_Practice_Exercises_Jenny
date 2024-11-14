# Lists in Python
print()

# Example 01
roll_no = [1, 2, 3, 4, 5]
names = ["Jenny", "Ram", "Shyam"]
mix_list = [1, "Jenny", True, 10.10]
print(roll_no)  # [1, 2, 3, 4, 5]
print(roll_no[1])  # 2
print()

# Example 02
numbers = [10, 0, -1, 7]
print(numbers)  # [10, 0, -1, 7]
names = ["Jenny", "Krishna", "Ram"]
print(names)  # ['Jenny', 'Krishna', 'Ram']
mix_list = [1, "Jenny", True, 10.10]
print(mix_list)  # [1, 'Jenny', True, 10.1]
print(numbers[1])  # 0
# print(numbers[6]) // Error; Index is out of range
print(len(numbers))  # 4
print(numbers[-1])  # 7
print(
    numbers[::]
)  # Default Start is index 0, Default Length is size of the list, Jumping From One by One. [10, 0, -1, 7]
print(numbers[0:4])  # [10, 0, -1, 7] : Complete List
print(numbers[1:3])  # [0, 1]
print()

# Example 03
numbers = [10, 0, -1, 7, 8, 10, -7]  # Duplicates are allowed!
print(numbers[1:4])  # [0, -1, 7]
print(numbers[:5])  # [10, 0, -1, 7, 8]
print(numbers[0:5:2])  # [10, -1, 8]
print()

# Example 04
numbers.sort()  # Sorting the List.
print(numbers)  # [-7, -1, 0, 7, 8, 10, 10]
# print(numbers.sort()) // Doesn't Support
numbers.reverse()  # Reverse the List.
print(numbers)  # [10, 10, 8, 7, 0, -1, -7]
# print(numbers.reverse()) // Doesn't support!
print()

# Example 05
print("Minimum Value of the List: " + str(min(numbers)))  # -7
print("Maximum Value of the List: " + str(max(numbers)))  # 10
mix_list = [1, "Jenny", True, 10.10]
# mix_list.sort() // With Boolean and String, Sort will not work!
print(mix_list)
numbers.append(20)  # Adding one value to the last of the list
print(numbers)  # 10, 10, 8, 7, 0, -1, -7, 20
numbers.insert(
    2, 25
)  # Add an element to specified index. Will not remove existence elements.
print(numbers)  # [10, 10, 25, 8, 7, 0, -1, -7, 20]
numbers.extend([50, 95, 100,
                2000])  # Will add more than one value at once to the end!
print(numbers)
numbers[
    1] = 22  # Changing a value without adding new element in specified index
print(numbers)
numbers[1:4] = [
    45, 46, 47
]  # Change the values from index 1 to 4 without adding new elements!
print(numbers)  # [10, 45, 46, 47, 7, 0, -1, -7, 20, 50, 95, 100, 2000]
numbers.remove(0)  # Will remove only first occurence!
print(numbers)  # [10, 45, 46, 47, 7, -1, -7, 20, 50, 95, 100, 2000]
numbers.extend([44, 44])
print(numbers)  # [10, 45, 46, 47, 7, -1, -7, 20, 50, 95, 100, 2000, 44, 44]
numbers.remove(44)
print(numbers)  # [10, 45, 46, 47, 7, -1, -7, 20, 50, 95, 100, 2000, 44]
print()

# Exercise 06
numbers = [10, 0, -1, 7, 8, 10, -67, 8]
print(numbers)  # [10, 0, -1, 7, 8, 10, -67, 8]
numbers.remove(10)  # Will remove only first element of the duplicates!
print(numbers)  # [0, -1, 7, 8, 10, -67, 8]
numbers.pop()  # Remove the last element
print(numbers)  # [0, -1, 7, 8, 10, -67]
print(numbers.pop())  # Return the removed element!
numbers.pop(1)
print(numbers)  # [0, 7, 8, 10]
numbers.pop(3)
print(numbers)  # [0, 7, 8]
print(numbers.count(7))  # 1
numbers.append(7)
print(numbers.count(7))  # 2
