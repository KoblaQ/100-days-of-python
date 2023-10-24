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

def total_money():
    """ Returns the total of money input into the coffee machine"""
    global money

    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickles + pennies
    return total

def resources_check(ingredients):
    """ Checks to see if there are enough ingredients to make the coffee and returns True of False"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def transaction_success(money_received, coffee_price):
    """ Returns True when payment is successful and False when payment is not enough """
    if money_received >= coffee_price:
        change = round(money_received - coffee_price, 2)
        print(f"Here is ${change} in change.")
        global money
        money += coffee_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(coffee_name, order_ingredients):
    """ Deduct the used ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name} ☕")


money = 0
turned_off = False


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while not turned_off:
    answer = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if answer == "off":
        turn_off = True
        print("Turned off")
    elif answer == "report":
        # TODO: 3. Print report of all coffee machine resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        # TODO: 4. Check resources sufficient?.
        coffee_type = MENU[answer]
        if resources_check(coffee_type['ingredients']):
            # TODO: 5. Process coins.
            payment = total_money()
            # TODO: 6. Check transaction successful?
            if transaction_success(payment, coffee_type["cost"]):
                # TODO: 7.  Make Coffee
                make_coffee(answer, coffee_type['ingredients'])
