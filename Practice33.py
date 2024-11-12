# Coding Exercise 09
print()
print("Pizza Order Program")
print("===================")
print()
print("(A) Select your preferred pizza size.")
print()
print("01. Small Pizza  :- Rs. 100.00")
print("02. Medium Pizza :- Rs. 200.00")
print("03. Large  Pizza :- Rs. 300.00")
print()
size = input("Enter your preferred pizza size (S / M / L)            :- ")
print()
print("(B) Add pepperoni to the pizza.")
print()
print("01. Add Pepperoni to the Small Pizza             :- Rs. 30.00")
print("02. Add Pepperoni to the Medium and Large Pizzas :- Rs. 50.00")
print()
pepperoni = input("Do you want to add pepperoni for the pizza? (Y / N)    :- ")
print()
print("(C) Add extra cheese to the pizza.")
print()
print("01. Add Extra Cheese for any Pizza :- Rs. 20.00")
print()
cheese = input("Do you want to add extra cheese for the pizza? (Y / N) :- ")
print()
if (size in ("S", "s", "M", "m", "L", "l")
        and pepperoni in ("Y", "y", "N", "n")
        and cheese in ("Y", "y", "N", "n")):
    bill = 0
    if (size in ("S", "s")):
        bill += 100
        print(f"Small Pizza            :- Rs. {bill}.00")
    elif (size in ("M", "m")):
        bill += 200
        print(f"Medium Pizza           :- Rs. {bill}.00")
    else:
        bill += 300
        print(f"Large Pizza            :- Rs. {bill}.00")
    if (pepperoni in ("Y", "y")):
        if (size in ("S", "s")):
            bill += 30
            print(f"Pepperoni Added        :- Rs.  {30}.00")
        else:
            bill += 50
            print(f"Pepperoni Added        :- Rs.  {50}.00")
    if (cheese in ("Y", "y")):
        bill += 20
        print(f"Extra Cheese Added     :- Rs.  {20}.00")
    if (size in ("S", "s")):
        print(f"Your Total Bill        :- Rs. {bill}.00\n")
    elif (size in ("M", "m")):
        print(f"Your Total Bill        :- Rs. {bill}.00\n")
    elif (size in ("L", "l")):
        print(f"Your Total Bill        :- Rs. {bill}.00\n")
else:
    print("Incorrect Input! Please try again!")
print("Thank you for choosing us!")
print("=============================================================")
