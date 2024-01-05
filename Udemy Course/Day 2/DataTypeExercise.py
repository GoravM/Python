two_diggit_number = input()

 # ex input: 39
 # output:  3 + 9 = 12
 ############################################

strnum = str(two_diggit_number)

# get 1st and 2nd position number and convert into int
num1 = int(strnum[0])
num2 = int(strnum[1])

# print ans
print(num1 + num2)
 
