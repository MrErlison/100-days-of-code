# 🚨 Don't change the code below 👇
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Important you are not allowed to use the max or min functions. 
high_score = 0
for i in student_scores:
    if high_score < i:
        high_score = i

print(f"The highest score in the class is: {high_score}")