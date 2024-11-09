# Exercise 19
print()
a = 5
print(a)  # 5
# 5 = a -> Error of Assignment
# 5 = 5 -> Error of Assignment
a = a + 2
print(a)  # 7
a += 2
print(a)  # 9
a = a / 2
print(a)  # 4.5
a /= 2
print(a)  # 2.25
a, b, c = 5, 6, 7
print(a, b, c) # 5 6 7
# 5 = 6 -> Error of Assignment
a, b, c = 5, 4, 6
print(a, b, c) # 5 4 6
a, b = 4, 3
print(a, b) # 4 3
a += 2
print(a) # 6
c = a + b
a += 2 
c += a 
print(c) # 17
a, b = 4, 3
c = a + b
a += 2
c /= a
print(c) # 1.1667
c = 7
c //= a
print(c) # 1