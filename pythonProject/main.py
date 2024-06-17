# TODO 1. give out the list of items, their contains and their prices
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total documented from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?:\n")) * 0.25
    total += int(input("how many dimes?:\n")) * 0.10
    total += int(input("how many nickles?:\n")) * 0.05
    total += int(input("how many pennies?:\n")) * 0.01
    return total

def is_transaction_successful(amount_received, drink_cost):
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f'here is your ${change} in change.')
        global profit
        profit += amount_received
        return True
    else:
        print("Sorry not enough money. Money refunded!")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("here is your drink")
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):\n')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {round(profit,2)}$")


    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

