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
is_on = True


def check_resources(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} water.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How man quarters?: ")) * 0.25
    total += int(input("How man quarters?: ")) * 0.1
    total += int(input("How man quarters?: ")) * 0.05
    total += int(input("How man quarters?: ")) * 0.01
    return total


def is_transaction_success(money_received, drink_cost):
    """Return True when the payment is accepted. or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffee.")


while is_on:
    # TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    coffee_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2: Turn off the Coffee Machine by entering "off" to the prompt.
    if coffee_selection == "off":
        is_on = False

    # TODO 3: Print report.
    elif coffee_selection == 'report':
        print(f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: ${profit}
    """)
    else:
        drink = MENU[coffee_selection]
        # TODO 4: Check resources sufficient?
        if check_resources(drink["ingredients"]):
            # TODO 5: Process coins
            payment = process_coins()
            # TODO 6: Check transaction successful?
            if is_transaction_success(payment, drink["cost"]):
                # TODO 7: Make Coffee
                make_coffee(coffee_selection, drink["ingredients"])
