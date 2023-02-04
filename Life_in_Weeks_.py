print("program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.")
age = input("What is your current age? ")
age1 = 90-int(age)
days = int(age1)*365
weeks = int(age1)*52
months = int(age1)*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")