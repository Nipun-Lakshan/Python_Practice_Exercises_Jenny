# Coding Exercise 13
print()
l1 = ['😃', '😃', '😃']
l2 = ['😃', '😃', '😃']
l3 = ['😃', '😃', '😃']
final_list = [l1, l2, l3]
print("3 x 3 Matrix Placement Game")
print("===========================")
print()
print(l1)
print(l2)
print(l3)
print()
input = input("Enter the position where you want to hide money: ")
length = len(input)
row = -25
column = -30
if (length == 2):
    row = int(input[0])
    column = int(input[1])
print()
if (row in (1, 2, 3) and column in (1, 2, 3) and length == 2):
    final_list[row - 1][column - 1] = '⚽'
    print("3 x 3 Matrix Placement")
    print("======================")
    print()
    print(l1)
    print(l2)
    print(l3)
    print()
    print("Thank you! Come again!")
    print("======================")
else:
    print("Invalid Input! Please try again.")
    print("================================")
