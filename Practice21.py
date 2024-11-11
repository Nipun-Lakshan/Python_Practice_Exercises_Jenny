# Sample code for round() function in Python
print()
# Case 1: Positive n (round to decimal places)
print(round(123.456789, 2))  # Expected: 123.46
print(round(123.455789, 2))  # Expected: 123.46
print(round(123.445789, 2))  # Expected: 123.45
print(round(123.445, 2))  # Expected: 123.44
print(round(123.456789, 4))  # Expected: 123.4568
print()

# Case 2: n as zero (round to nearest integer)
print(round(123.456789, 0))  # Expected: 123.0 (float because of decimal point)
print(round(123.456789))  # Expected: 123
print()

# Case 3: Negative n (round to the nearest 10, 100 and etc.)
print(round(1234.56789, -1))  # Expected: 1230.0
print(round(1234.56789, -2))  # Expected: 1200.0
print(round(1234.56789, -3))  # Expected: 1000.0
print(round(1234.56789, -4))  # Expected: 0.0
print()

# Case 4: No n provided (defaults to rounding to nearest integer)
print(round(123.456))  # Expected: 123
print(round(123.556))  # Expected: 124
print(round(122.5))  # Expected: 122
print(round(122.56))  # Expected: 123
print()

# Case 5: Tie-breaking case with "round half to even" (banker's rounding)
print(round(2.5))  # Expected: 2 (even number)
print(round(3.5))  # Expected: 4 (even number)
print(round(2.65, 1))  # Expected: 2.6 (even rounding at one decimal place)
print(round(2.75, 1))  # Expected: 2.8 (even rounding at one decimal place)
print()

# Case 6: If the digits parameter exceeds the digits of the number
print(round(123.45, -4))  # Expected: 0.0
print(round(45.6789, -2))  # Expected: 0.0 (since rounding to hundreds place)
print()

# Case 7: Integer input for number (result will be integer regardless of n)
print(round(150, 2))  # Expected: 150
print(round(150, -1))  # Expected: 150
print(round(150, -2))  # Expected: 200 (rounding up to nearest hundred)
print()
