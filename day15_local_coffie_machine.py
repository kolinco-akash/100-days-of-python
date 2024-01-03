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
            print(f"Sorry, we don't have enough {item}.")
            return False
    return True

def process_coins():
    print("Please enter coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if payment >= drink["cost"]:
                    resources["water"] -= drink["ingredients"]["water"]
                    resources["milk"] -= drink["ingredients"].get("milk", 0)
                    resources["coffee"] -= drink["ingredients"]["coffee"]
                    change = payment - drink["cost"]
                    profit += drink["cost"]
                    print(f"Here is ${change:.2f} in change.")
                    print(f"Enjoy your {choice}!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Sorry, not enough resources to make that drink.")
        else:
            print("Invalid choice. Please select a valid option.")
