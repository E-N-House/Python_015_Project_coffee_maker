from machine_data import resources, format_resources, is_enough_resources
from coin_data import COINS
from menu_data import MENU, format_menu, pull_ingredient_list


def start_machine():
    is_on = True
    while is_on:
        # Ask the user what they want to do and change it to lowercase
        user_request = input("“What would you like? (espresso/latte/cappuccino):  ").lower()
        # print a report of what it has in stock
        if user_request == "report":
            # Format the resources for printing
            print(format_resources(resources))
        # Turn off the Coffee Machine by entering “off” to the prompt.
        elif user_request == "off":
            is_on = False
            return
        elif user_request == "menu":
            # TODO load if in stock
            # format menu as name and price
            print(format_menu(MENU))
        # Checks if user request is in menu
        elif user_request in MENU:
            # TODO 2. when user orders need to check it has enough to make drink before taking money
            # grab the ingredient list for item
            ingredient_list = pull_ingredient_list(user_request)
            is_enough_resources(ingredient_list=ingredient_list, inventory=resources)
            # compare the ingredient list with the resources




start_machine()

# TODO 2. when user orders need to check it has enough to make drink before taking money
# TODO 3 takes penny nickle dime quarter
# TODO 2.1 if yes ask for payment and then return change at end
# TODO 2.2 if not enough money refund
# TODO 3. make the drink and update the resources
