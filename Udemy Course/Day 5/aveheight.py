student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
###################################################

sumHeight = 0

for n in student_heights:
    sumHeight += n

ave = round(sumHeight/len(student_heights))
print(ave)