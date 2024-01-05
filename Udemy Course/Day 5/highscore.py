student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
###############################

hi_score  = 0

for n in student_scores:
    if n > hi_score:
        hi_score = n

print(hi_score)