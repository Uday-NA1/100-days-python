# Procedural - functions and sequential steps
# OOP - classes and objects

# Objects have Attributes (variables) and Methods (functions)
# Classes are the blueprints used to create multiple objects

# A python package is a lot of files packaged together

from turtle import Turtle, Screen

timmy = Turtle() # Turtle is the class, timmy is the object
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight) # object.attribute
my_screen.exitonclick()   # object.method(parameters)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)

from classes import *

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

over = False
coffee_maker.report()
money_machine.report()

while not over:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        over = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)