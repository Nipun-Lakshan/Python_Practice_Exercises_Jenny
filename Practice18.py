# Exercise 24
print()
a = 5
b = 5
print(a is b)  # True
print(a is not b)  # False
print(id(a))  # 140709584299048
print(id(b))  # 140709584299048
print(id(a) == id(b))  # True
print(a == b)  # True

print()
a = 10
print(id(a))  # 140709584299208
a = 9
print(id(a))  # 140709584299176
print(a is a)  # True

print()
a = 5
b = "5"
print(a is b)  # False
print(a is not b)  # True
print(id(a))  # 140709584299048
print(id(b))  # 140709584361328
print(id(a) == id(b))  # False
print(a == b)  # False

print()
a = 10
print(id(a))  # 140709584299208
print(id(10))  # 140709584299208
print(id(a) == id(10))  # True

print()
a = 10
b = 10.12
print(a is b)  # False

print()
a = 10
b = "10"
print(a is b)  # False
print(a is not b)  # True

print()
a = 5
print(id(a))  # 140709584299048
a = 6
print(id(a))  # 140709584299080
# Int is an immutable object.

print()
a = 5
b = 5.0
print(id(a))  # 140709584299048
print(id(b))  # 2421072639216
print(a is b)  # False

print()
a = 5
print(id(a))  # 140709584299048
a = 8
print(id(a))  # 140709584299144
print(a is a)  # True
