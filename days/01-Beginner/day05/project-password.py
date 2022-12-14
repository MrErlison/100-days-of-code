# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random, string

print('Welcome to Password Generator!')

password = ""
total_letters = int(input('How many letters would you like in your password? '))
total_symbols = int(input('How many symbols would you like? '))
numbtotal_numbers = int(input('How many numbers would you like? '))

password += ''.join(random.choice(string.ascii_letters) for i in range(total_letters)) 

password += ''.join(random.choice(string.punctuation) for i in range(total_symbols)) 

password += ''.join(random.choice(string.digits) for i in range(total_numbers)) 

password = ''.join(random.choice(password) for i in range(len(password))) 

print(f'Your password is: {password}')
