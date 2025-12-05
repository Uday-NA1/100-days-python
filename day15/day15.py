MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    },
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

over = False
profit = 0

def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")

def sufficient_resources(drink):
    depleted = []
    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
            depleted.append(ingredient)

    return depleted

def proccess_coins(quarters_amount, dimes_amount, nickles_amount, pennies_amount):
    total = (quarters_amount * 0.25) + (dimes_amount * 0.10) + (nickles_amount * 0.05) + (pennies_amount * 0.01)
    return total

def successful_order(drink, amount, depleted):
    failed = False
    if depleted:
        for i in depleted:
            print(f"Sorry there is not enough: {i}")
            failed = True

    if amount < MENU[drink]['cost']:
        failed = True
        print("Sorry that's not enough money. Money refunded.")

    elif amount > MENU[drink]['cost']:
        diff = amount - MENU[drink]['cost']
        print(f"Here is ${round(diff, 2)} in change.")

    return failed

def run_machine(drink):
    global resources, profit
    print("Please insert coins:")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    failed = successful_order(drink, proccess_coins(quarters, dimes, nickles, pennies), sufficient_resources(drink))
    if not failed:
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']
        profit += MENU[drink]['cost']

        print(f"Here is your {drink}. Enjoy!")

while not over:
    request = input("What would you like to have? (espresso / latte / cappuccino): ").lower()

    if request == "espresso":
        run_machine(request)
    elif request == "latte":
        run_machine(request)
    elif request == "cappuccino":
        run_machine(request)
    elif request == "report":
        print_report()
    elif request == "off":
        over = True