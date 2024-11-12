# Coding Exercise 07
print()
print("BMI Calculator")
print("==============")
print()
weight = float(input("Enter your weight in Kg: - "))
height = float(input("Enter your height in m: - "))
print()
bmi_value = round(weight / (height**2))
print("Your BMI Value: - " + str(bmi_value))
if (bmi_value < 18.5):
    print("Result: - Underweight")
elif (bmi_value <= 24.9):
    print("Result: - Normal Weight")
elif (bmi_value <= 29.9):
    print("Result: - Overweight")
else:
    print("Result: - Obese")
