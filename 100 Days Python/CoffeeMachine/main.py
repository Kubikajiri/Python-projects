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


def check_resources(storage_resources, chosen_coffee):
    """
    Check if the resources are sufficient to make a chosen coffee
    :param storage_resources:
    :param chosen_coffee:
    :return:
    """
    for key in MENU:
        coffee_needs = MENU[key]["ingredients"]
        if key != chosen_coffee:
            continue
        else:
            for ingredient in coffee_needs:
                if coffee_needs[ingredient] > storage_resources[ingredient]:
                    print(f"Sorry, we're out of {ingredient}")
                    return False
                else:
                    return True






def coins():
    """
    Requests the client to put the coins into the machine and counts it.
    After the money is put, the function counts the change and returns it,
    or tells the user if he put not enough money.

    After, it will subtract the used resources from the "resources" dictionary
    """

    chosen_coffee_cost = MENU[what_coffee]["cost"]
    print(chosen_coffee_cost)

    quarter = 0.25
    dime = 0.1
    nickle = 0.05
    penny = 0.01
    print("Please enter coins")

    counting = False
    while not counting:
        quarters = int(input("How many quarters? ")) * quarter
        dimes = int(input("How many dimes? ")) * dime
        nickles = int(input("How many nickles? ")) * nickle
        pennies = int(input("How many pennies? ")) * penny
        return quarters + dimes + nickles + pennies


def process_coffee(coffee):
    """
    This funcion prints the coffee the user has requested and subtracts its resourses feom the reservoir.
    :param coffee:
    :return:
    """
    for key in MENU[coffee]["ingredients"]:
        resources[key] = resources[key] - MENU[coffee]["ingredients"][key]

    print(f"Here is your {coffee}! Have a nice day!")


off = False

while not off:
    if "report":
        print(resources)
    what_coffee = input("What would you like? (espresso, latte, cappuccino)? ")
    if not check_resources(resources, what_coffee):
        off = True
    else:
        coffee_cost = MENU[what_coffee]["cost"]
        money_put = coins()
        if money_put > coffee_cost:
            change = coins() - coffee_cost
            print(f"Here's your change {change}.")
        else:
            more = input(f"You need {money_put - coffee_cost} more. Do you want to put more money? y/n").lower()
            if more == "y":
                money_put += coins()
        print(f"Processing coffee ... -> {what_coffee}")
        process_coffee(what_coffee)