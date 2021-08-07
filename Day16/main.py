from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()

is_on = True

while is_on:
    options = menu.get_items()
    coffee_selection = input(f"What would you like? ({menu.get_items()}): ").lower()
    if coffee_selection == "off":
        is_on = False
    elif coffee_selection == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(coffee_selection)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
