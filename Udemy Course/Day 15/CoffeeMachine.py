MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print({f"sorry there isnt enough {item}."})
            return False
    return True


def coins():
    print("Please inser coins.")
    total = 0.25 * int(input("How many Quaters?: "))
    total += 0.1 * int(input("How many Dimes?: "))
    total += 0.05 * int(input("How many Nickels?: "))
    total += 0.01 * int(input("How many Pennies?: "))
    return total

def transaction(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not ewnough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}g")
        print(f"Water: ${profit}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
