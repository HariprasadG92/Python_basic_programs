#You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
rand_int = random.randint(0,(len(names))-1 )
rand_name = names[rand_int]
print(f"{rand_name} is going to buy the meal today!")
