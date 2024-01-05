print("The love calculator")
name1 = input()
name2 = input()
####################################

combine = name1 + name2 ## combines name 1 and name 2

lower = combine.lower() # makes all letters into lowercase

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

truescore = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

lovescore = l + o + v + e

score = int(str(truescore) + str(lovescore))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go togheter like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright togheter.")
else:
    print(f"Your score is {score}.")