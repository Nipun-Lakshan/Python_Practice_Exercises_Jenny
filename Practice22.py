# round() in Python
print()
# Example 01
print(round(21.3333))  # 21
print(round(21.3333, 2))  # 21.33
print()

# Example 02
print(round(7))  # 7
print(type(round(7)))  # int
print(round(7, 2))  # 7
print(type(round(7, 2)))  # int
print(round(7.61))  # 8
print(type(round(7.61)))  # int
print(round(2.6666, 2))  # 2.67
print(type(round(2.6666, 2)))  # float
print(round(2.6657, 0))  # 3.0
print(type(round(2.6657, 0)))  # float
print(round(7.5))  # 8
print(type(round(7.5)))  # int
print()

# Example 03
print(round(6.5))  # 6
print(round(11.5))  # 12
print(round(12.5))  # 12
print()

# Example 04
print(round(674, 2))  # 674
print(round(674, 0))  # 674
print(round(674, -1))  # 670
print(round(674, -2))  # 700
print(round(674, -3))  # 1000
print(round(674, -4))  # 0
print()

# Example 05
print(round(665, -1))  # 660
print(round(675, -1))  # 680
print(round(6.75, 1))  # 6.8
print(round(6.85, 1))  # 6.8
print(round(6.741012, 1))  #  6.7
print(round(1212, -2))  # 1200
print(round(644, -2))  # 600
print()

# Example 06
print(round(-8 / 3))  # -2.6667 -> -3
print(round(-1.5))  # -2
print(round(-8 / 3, 2))  # 2.6667 -> -2.67
print()

# Example 07
print(round(7.6666, 2))  # 7.67
print(type(round(7.6666, 2)))  # float
print(round(7.6666))  # 8
print(type(round(7.6666)))  # int
print(round(-2.5))  # -2
print(round(2.6645786, 2))  # 2.66
print(round(7.6))  # 8
print()

# Example 08
print(round(8.5))  # 8
print()
