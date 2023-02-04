print("Welcome to Tip Caculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
person = int(input("How many people to split the bill? "))
tip1 = tip/100
tot_tip1 = bill * tip1
bill1 = bill + float(tot_tip1) 
split = float(bill1) / person
split1 = round(split, 2)
split1 = "{:.2f}".format(split1)
print(f"Each person should pay: ${split1}")

