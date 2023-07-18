MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}


def format_menu(items):
    """Takes in menu dictionary and formats it as 'Key: value' on separate lines and returns the string"""
    menu_with_prices = ""
    for thing in items:
        cost = items[thing]['cost']
        menu_with_prices += f"{thing.capitalize()}: ${cost}\n"
    return menu_with_prices


def pull_ingredient_list(item):
    global MENU
    ingredient_list = MENU[item]['ingredients']
    return ingredient_list
