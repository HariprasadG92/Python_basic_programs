height = int(input("Enter height in cm: "))
age = int(input("Enter your age: "))
bill = 0
if height >= 120:
    print("You can ride the roller coster")
    if age < 12:
        bill = 5
        print("Childrens tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12")
    photo = input(" Do you want a photo taken for +$3? Y or N")
    if photo == "Y":
        bill += 3
    print(f"Final amount {bill}")
else:
    print("Your short for this ride...")
