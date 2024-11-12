# Coding Exercise 8
print()
print("Determine Whether a Year is a Leap Year or Not")
print("==============================================")
print()
year = int(input("Enter a year:- "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is a not a leap Year!")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is a not a leap year!")
