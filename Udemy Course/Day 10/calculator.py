# Calculator

# Add
def add (n1, n2):
    return n1 + n2

# Substract
def sub(n1 , n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}


endfinal = False
def calculator():
    num1 = float(input("What's the first number?: "))

    endfinal = False

    while not endfinal:

        for sign in operations:
            print(sign)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        function = operations[operation_symbol]
        answer = function(n1= num1, n2= num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        endstat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if endstat == "n":
            endfinal = True
            calculator()
        else:
            num1 = answer
            num2 = float(input("What's the next number?: "))

calculator()