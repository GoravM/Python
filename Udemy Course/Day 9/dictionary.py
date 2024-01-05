programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# print a certain information from the dictionary
# print(programming_dictionary["Bug"])

# add a new item in disctionary with definition
# programming_dictionary["Bruh"] = "Bruh Bruh"

# Wipe an existing dictionary by redefining it
# programming_dictionary = {}

# edit an item in dictionary
# programming_dictionary["Bug"] = "Meow"

# Loop through a dictionary only definition
# for thing in programming_dictionary:
#     print(programming_dictionary[thing])

# Loop through a dictionary only word
# for thing in programming_dictionary:
#     print(thing)

# Loop though a dictionary both word and definition
for thing in programming_dictionary:
    print(thing + " : " + programming_dictionary[thing])