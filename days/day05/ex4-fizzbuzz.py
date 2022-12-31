#Write your code below this row 👇
#for number in range(1,101):
#    if (number % 3 == 0) and (number % 5 == 0):
#        print("FizzBuzz")
#    elif number % 3 == 0:
#        print("Fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print(number)

for i in range(1, 101): 
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)
