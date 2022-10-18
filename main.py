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

money = 0


# TODO: 3. Print report.
def print_report():
    """This function prints out the report regarding how much of the ingredients are left"""
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    print(f"Water: {water_left}ml")
    print(f"Milk: {milk_left}ml")
    print(f"Coffee: {coffee_left}mg")
    print(f"Money: ${money}")


# TODO: 4. Check resources sufficient?
def check_resources(drink):
    """This function checks if the coffee machine has enough of the ingredients to make a drink and returns True if
        so and returns False if otherwise"""
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']

    if drink == "espresso":
        water_drink = MENU[drink]['ingredients']['water']
        coffee_drink = MENU[drink]['ingredients']['coffee']
        if water_drink > water_left:
            print("Sorry there is not enough water.")
            return False
        elif coffee_drink > coffee_left:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    elif drink == "latte":
        water_drink = MENU[drink]['ingredients']['water']
        coffee_drink = MENU[drink]['ingredients']['coffee']
        milk_drink = MENU[drink]['ingredients']['milk']
        if water_drink > water_left:
            print("Sorry there is not enough water.")
            return False
        elif coffee_drink > coffee_left:
            print("Sorry there is not enough coffee.")
            return False
        elif milk_drink > milk_left:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True

    elif drink == "cappuccino":
        water_drink = MENU[drink]['ingredients']['water']
        coffee_drink = MENU[drink]['ingredients']['coffee']
        milk_drink = MENU[drink]['ingredients']['milk']
        if water_drink > water_left:
            print("Sorry there is not enough water.")
            return False
        elif coffee_drink > coffee_left:
            print("Sorry there is not enough coffee.")
            return False
        elif milk_drink > milk_left:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True


# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
def process_coins(drink):
    global money
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    drink_price = MENU[drink]['cost']
    if total < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        change = round(total - drink_price, 1)
        money += drink_price
        print(f"Here is ${change} in change.")


# TODO: 7. Make Coffee.
def make_coffee(drink):
    global resources
    if drink == "espresso":
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']


def coffee_machine():
    while True:
        # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        machine = input("    What would you like? (espresso/latte/cappuccino): ").lower()
        if machine == 'report':
            print_report()
        elif machine == 'off':
            # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
            break
        else:
            enough = check_resources(machine)
            if enough:
                process_coins(machine)
                make_coffee(machine)
                print(f"Here is your {machine}. Enjoy!")


coffee_machine()
