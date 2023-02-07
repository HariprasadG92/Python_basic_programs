print("With The Love Calculator you can calculate the probability of a successful relationship between two people. \n The Love Calculator is an affective way to get an impression of what the chances are on a relationship between two people.")
name1 = input("Enter your name: ")
name2 = input("Enter thier name: ")
combine_name = name1 + name2
lc_name = combine_name.lower()
t = lc_name.count("t")
r = lc_name.count("r")
u = lc_name.count("u")
e = lc_name.count("e") 
true = t + r + u + e

l = lc_name.count("l")
o = lc_name.count("o")
v = lc_name.count("v")
e = lc_name.count("e")
love = l + o + v + e

total = str(true) + str(love)
total_int = int(total)
if total_int <10 or total_int>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total_int >=40 and total_int<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
