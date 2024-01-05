import random

num = random.randint(0,3)

fruits = ["apple", "cherry", "banana", "orange"]

print(fruits)

# print(fruits[-1])

fruits.append("watermelon")
print(fruits)

fruits.extend(["grape", "starfruit"])
print(fruits)