# n/3 "fizz"
# n/5 "buzz"
# n/3 and 5 "fizzbuzz"

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    
    elif n % 3 == 0:
        print("Fizz")
    
    elif n % 5 == 0:
        print("Buzz")
    
    else:
        print(n)
