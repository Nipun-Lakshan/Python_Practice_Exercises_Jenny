# Elif & Nested If Statements
print()

# Example 01
height = int(input("Enter your height in feet: - "))
if (height >= 3):
    print("You can ride the roller coaster!")
    print()
    age = int(input("Enter your age: - "))
    if (age <= 18):
        print("Pay Rs. 250/=")
    else:
        print("Pay Rs. 500/=")
else:
    print("You can't ride the roller coaster!")
print("Bye!")
print("===================================")
print()

# Example 02
height = int(input("Enter your height in feet: - "))
if (height >= 3):
    print("You can ride the roller coaster!")
    print()
    age = int(input("Enter your age: - "))
    if (age <= 12):
        print("Pay Rs. 150/=")
    elif (age <= 18):
        print("Pay Rs. 250/=")
    else:
        print("Pay Rs. 500/=")
else:
    print("You can't ride the roller coaster!")
print("Bye!")
print("===================================")
print()

# Example 03
number = int(input("Enter an Integer (1 - 10): - "))
if (number == 1):
    print("Congratulations! You have won a gift voucher worth Rs. 1000/=")
elif (number == 2):
    print("Congratulations! You have won a gift voucher worth Rs. 2000/=")
elif (number == 3):
    print("Congratulations! You have won a gift voucher worth Rs. 3000/=")
elif (number == 4):
    print("Congratulations! You have won a gift voucher worth Rs. 4000/=")
else:
    print("Sorry! Please try again!")
print("Bye!")
print("==============================================================")
print()

# Example 04
a = int(input("Enter an Integer: - "))
if (a % 2 == 0):
    print(f"{a} is an even number!")
    if (a > 10):
        print(f"{a} is greater that 10. That's great!")
print("Bye!")
print("============================")
print()
