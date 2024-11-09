# Exercise 17
print()
print(5 + 2 * 3 - 1 + 10 / 5)  # Answer :- 12.0
print(5 + 2 * (3 - 1) + 10 /
      5)  # Answer :- 11.0 // Only adding one parenthesis for given expression!

print()
print(5 + 3)  # 5 + 3 = 8
print(10 - 4)  # 10 - 4 = 6
print(7 * 2)  # 7 * 2 = 14
print(9 / 2)  # 9 / 2 = 4.5
print(9 % 2)  # 9 % 2 = 1
print(9 // 2)  # 9 // 2 = 4
print(3**2)  # 3 ** 2 = 9

print()
print(5 / 2)  # 5 / 2 = 2.5
print(4 / 2)  # 4 / 2 = 2.0
print(4 // 2)  # 4 //2 = 2
print(2**3)  # 2 ** 3 = 8
print(4**2)  # 4 ** 2 = 16

print()
print(5 + 2)  # 7
print(5 - 2)  # 3
print(5 / 2)  # 2.5
print(4 / 2)  # 2.0
print(4 // 2)  # 2
print(4**2)  # 16
print(2**3)  # 8
print(5 % 2)  # 1

print()
a = 5
b = 2
print(a / b)  # 5 / 2 = 2.5
print()

# BMI Calculator
print("BMI Calculator")
print("==============")
print()
weight = input("Enter your weight in Kg :- ")
height = input("Enter your heigh in m   :- ")
print()
print("Your BMI Value :- " + str(float(weight) / (float(height)**2)))
