height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight/height**2
bmi1 = round(bmi)
if bmi1 < 18.5:
    print(f"Your BMI is {bmi1}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi1}, you have a normal weight.")
elif bmi <30:
    print(f"Your BMI is {bmi1}, you are slightly overweight.")
elif bmi <35:
    print(f"Your BMI is {bmi1}, you are obese.")
else:
    print(f"Your BMI is {bmi1}, you are clinically obese.")
