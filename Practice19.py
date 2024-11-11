# Exercise 25
print()
String = "apple"
print("a" in String)  # True
print("b" not in String)  # True

print()
str_1 = "Jenny"
print("y" in str_1)  # True
print("nny" in str_1)  # True
print("Y" in str_1)  # False
print("Y" not in str_1)  # True
print("e" not in str_1)  # False

print()
list_1 = [1, 10, -1, 0, 17]
print(10 in list_1)  # True
print(10 not in list_1)  # False

print()
str_2 = "Jayanti Khatri"
print("y" in str_2)  # True
print("yan" in str_2)  # True
print("JayantiKhatri" in str_2)  # False
print("Jayanti Khatri" in str_2)  # True
print("Yan" in str_2)  # False

print()
list_2 = [1, 10, 0, -5, 2]
print(0 in list_2)  # True
print(-1 in list_2)  # False

print()
str_3 = "Jenny Khatri"
print("j" in str_3)  # False
print("Jen" in str_3)  # True
print("JennyKhatri" in str_3)  # False
print("Jenny Khatri" in str_3)  # True
print("J" not in str_3)  # False
print("b" not in str_3)  # True

print()
str_4 = "Hello"
print("H" not in str_4)  # False

print()
list_3 = [2, 67, 0, -7, 45]
print(2 in list_3)  # True
print(20 in list_3)  # False
print(20 not in list_3)  # True
print(-7 not in list_3)  # False
