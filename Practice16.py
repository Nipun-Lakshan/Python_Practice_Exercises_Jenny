# Exercise 22
print()
a, b = 5, 4
print(a > 4 and b < 10)  # True
print(a > 4 and b < 3)  # False
print(a < 4 or b < 3)  # False
print(a < 4 or b < 13)  # True
print(not (a))  # False
a = False
print(not (a))  # True

print()
a, b = 4, 3
print(a < 3 and b == 3)  # False
print(a < 3 or b == 3)  # True
print(not (a))  # False
c = True
print(not (c))  # False
print(a <= 4 and c)  # True
print(a < 4 and c)  # False
print(a < 4 or c)  # True

print()
a, b = 5, 4
print(a and 5)  # 5
print(a < 5 and b == 4)  # False
print(a <= 5 and b == 4)  # True
print(a < 5 or b == 4)  # True
print(5 and 4)  # 4
print(0 and 4)  # 0
print(0 or 4)  # 4
print(not (a))  # False
a = False
print(not (a))  # True
