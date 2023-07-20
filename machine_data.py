resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def format_resources(items):
    """Takes in dictionary of items and formats it and returns the string"""
    return f"Water: {items['water']}ml\nMilk: {items['milk']}ml\nCoffee: {items['coffee']}g\nMoney: ${items['money']}"


def format_unknown(items):
    """Takes in dictionary and formats it as 'Key: value' on separate lines and returns the string"""
    message = ""
    for thing in items:
        message += f"{thing.capitalize()}: {items[thing]}\n"
    print(message)


def is_enough_resources(ingredient_list, inventory):
    """takes in ingredient dictionary and inventory dictionary and
    checks if there is enough inventory to make item
    returns a boolean"""
    for ingredient in ingredient_list:
        if inventory[ingredient] >= ingredient_list[ingredient]:
            return True
        else:
            print(f"Sorry there is not enough {ingredient}.")
            return False


def update_inventory(payment, ingredient_list):
    """takes in the payment number and ingredient dictionary
    and returns an updated global resources/inventory
    NOTE Contains a global resources value"""
    global resources
    resources['money'] += payment
    for ingredient in ingredient_list:
        resources[ingredient] -= ingredient_list[ingredient]
        # resources[ingredient] -= ingredient
    return resources
