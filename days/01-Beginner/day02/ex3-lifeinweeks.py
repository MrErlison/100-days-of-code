# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
maximum_life_years = 90

#calculate totals
total_days = maximum_life_years * 365
total_weeks = maximum_life_years * 52
total_months = maximum_life_years * 12

#calculate time left
days_left = total_days - (age * 365)
weeks_left = total_weeks - (age * 52)
months_left = total_months - (age * 12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")