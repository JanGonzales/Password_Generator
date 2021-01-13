student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
Total_heights = 0
for var in student_heights:
    Total_heights += var

Average = Total_heights / n

print(Average)