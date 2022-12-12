# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3
elif add_pepperoni == "Y" and size == "S":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print("Your final bill is: ${bill:.2f}")
