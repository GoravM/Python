age = input("Your age is: ")
#######################################

weeks_till_90 = 90 * 52
age_weeks_pass = int(age) * 52

weeks_left = weeks_till_90 - age_weeks_pass

print(f"You have {weeks_left} weeks left.")