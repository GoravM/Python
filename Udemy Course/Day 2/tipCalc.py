print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip woulf you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = 1 + (tip / 100)

pay = round(((bill/people) * tip), 2)

print(f"Each person should pay: ${pay}")