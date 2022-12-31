# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()
true_world = "true"
love_world = "love"

first_digit = sum( [int(name.count(i)) for i in true_world] )
second_digit = sum( [int(name.count(i)) for i in love_world] )

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
