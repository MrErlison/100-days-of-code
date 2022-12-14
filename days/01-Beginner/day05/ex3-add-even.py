#Write your code below this row 👇

#numbers = [i for i in range(2, 101, 2)]
#total = sum(numbers)
#print(total)

total = 0
for i in range(2, 101):
    if i % 2 == 0:
        total += i
print(total)
