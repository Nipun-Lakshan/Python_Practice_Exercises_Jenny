# Multiple If Statements
print()

# Example 01
age = int(input("Enter your age: - "))
if (age < 12):
    print("Ticket Price is Rs. 150/=")
if (age < 18):
    print("Ticket Price is Rs. 250/=")
if (age >= 18):
    print("Ticket Price is Rs. 500/=")
print("Thank you!")
print("=========================")
print()

# Example 02
age = int(input("Enter your age: - "))
if (age < 12):
    print("Ticket Price is Rs. 150/=")
elif (age < 18):
    print("Ticket Price is Rs. 250/=")
elif (age >= 18):
    print("Ticket Price is Rs. 500/=")
print("Thank you!")
print("=========================")
print()

# Example 03
height = int(input("Enter your height: - "))
if (height >= 3):
    bill = 0
    print("You can ride the roller coaster!")
    print()
    age = int(input("Enter your age: - "))
    if (age < 12):
        print("Ticket Price is Rs. 150/=")
        bill = 150

    elif (age <= 18):
        print("Ticket Price is Rs. 250/=")
        bill = 250
    else:
        print("Ticket Price is Rs. 500/=")
        bill = 500
    print()
    want_a_Photo = input("Do you want a photo? (Y / N): - ")
    if (want_a_Photo == "y" or want_a_Photo == "Y"):
        bill += 50
    print(f"Your total bill is Rs. {bill}/=")
    print()
    print("Thank you...Enjoy your ride!")
else:
    print("You can't ride the roller coaster!")
    print()
    print("Thank you!")
print("==============================")
