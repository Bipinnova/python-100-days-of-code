MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 125,  
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,  
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,  
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total amount inserted by the user."""
    print("\nPlease insert coins.")

    total = int(input("How many ₹20 coins?: ")) * 20
    total += int(input("How many ₹10 coins?: ")) * 10
    total += int(input("How many ₹5 coins?: ")) * 5
    total += int(input("How many ₹2 coins?: ")) * 2
    total += int(input("How many ₹1 coins?: ")) * 1

    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted, otherwise False."""
    global profit

    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is ₹{change} in change.")
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. ₹{money_received} refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts ingredients and serves coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"☕ Here is your {drink_name}. Enjoy!\n")


is_on = True

while is_on:

    choice = input(
        "\nWhat would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        print("Coffee Machine is turning off...")
        is_on = False

    elif choice == "report":
        print("\n------ REPORT ------")
        print(f"Water  : {resources['water']} ml")
        print(f"Milk   : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} g")
        print(f"Money  : ₹{profit}")

    elif choice in MENU:

        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):

            payment = process_coins()

            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")