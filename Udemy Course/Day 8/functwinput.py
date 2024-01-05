# 0 input function
def greet():
    print("Hello")
    print("Waltuh")
    print("!")

# greet()

# 1 input function
def meet(name):
    print(f"Hello {name}")
    print(f"How are you {name}")
    print(f"Make me meth {name}")
    
# meet(input("What is your mame? "))
    
# 2 input function
def greet2(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")

uname = input("Your name is ")
ulocation = input("You live in ")
# greet2(uname, ulocation)

# this works correctly as intended as above
greet2(location= ulocation, name= uname) 
