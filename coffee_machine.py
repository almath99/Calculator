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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    """ A function that when the user chooses a drink,
    it checks if there are enough resources to make that drink."""

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False #to stop the machine
    return True

def check_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many ?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_inserted, drink_cost):
    """Accepts money or refunds it if it is insufficient."""

    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is your change ${change}.")
        global money
        money += money_inserted
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}☕")

def refill_resources():
    """Allows the user to add more resources to the machine."""
    refill_item = input("Which ingredient would you like to refill? (water/milk/coffee)").lower()
    if refill_item in resources:
        amount = int(input(f"How much {refill_item} would you like to add (ml/g)?: "))
        resources[refill_item] += amount
        print(f"{amount} units of {refill_item} added.")
    else:
        print(f"Sorry, {refill_item} is not a valid resource.")

is_on = True

while is_on:
    order = input("What would you like to drink☕? (espresso/latte/cappuccino): ")
    # For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine.
    if order == "off":
        is_on = False
    # a report that shows the current resource values
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(money, 2)}")
        refill = input("Would you like to refill any resources? (yes/no): ").lower()
        if refill == "yes":
            refill_resources()
    else:
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            payment = check_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])






