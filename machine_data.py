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
    for ingredient in ingredient_list:
        if inventory[ingredient] > ingredient_list[ingredient]:
            return True
        else:
            print(f"Sorry we do not have enough {ingredient}")
            return False
