print("Body mass index (BMI) is a person's weight sin kilograms divided by the square of height in meters.")
print("Enter Height and Weight for BMI calculation")
height = int(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight/height**2
print(bmi_as_int)
print("BMI values less than 18.5 kg/m² are considered underweight.\nBMI values from 18.5 kg/m² to 24.9 kg/m² are healthy.\nOverweight is defined as a body mass index of 25.0 to less than 30.0 kg/m²")
