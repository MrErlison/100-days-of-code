# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# person_who_pay = names[random.randint(0,len(names)-1)]
person_who_pay = random.choice(names)
print(f"{person_who_pay} is going to buy the meal today!")
