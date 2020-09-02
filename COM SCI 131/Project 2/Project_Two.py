# BMI Calculator

height = input("Enter your height in inches: ")
weight = input("Enter your weight in pounds: ")
bmi = (float(weight) * 703) / (float(height)**2)
print(bmi)

if bmi > 25:
    print("Your BMI indicates that you are overweight.")
elif bmi >= 18.5:
    print("Your BMI indicates that you are optimal weight.")
else:
    print("Your BMI indicates that you are underweight.")
