from machine_data import resources, format_resources, is_enough_resources, update_inventory
from coin_data import COINS, process_money
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
            print("Shutting down machine.")
            is_on = False
            return
        elif user_request == "menu":
            # TODO load if in stock
            # format menu as name and price
            print(format_menu(MENU))
        # Checks if user request is in menu
        elif user_request in MENU:
            # When user orders need to check it has enough to make drink before taking money
            # grab the ingredient list for item
            ingredient_list = pull_ingredient_list(user_request)
            # compare the ingredient list with the resources
            if is_enough_resources(ingredient_list=ingredient_list, inventory=resources):
                # store the data for easy access
                item_data = MENU[user_request]
                item_cost = item_data['cost']
                print(f"item data = {item_data}")
                resources_data = resources
                print(f"resource data = {resources_data}")
                # prompt user to enter money and save the amount to money variable
                print(f"Your {user_request} costs ${item_cost}.")
                money = process_money()
                # Check if enough money
                if money >= item_cost:
                    #  return change if there is any
                    if money > item_cost:
                        return_amount = round(money - item_cost, 2)
                        print(f"You overpaid here is money back ${return_amount}")
                    # reset money to be item_cost as that is how much is now in machine
                    money = item_cost
                    # update the machine inventory
                    update_inventory(payment=money, ingredient_list=ingredient_list)
                    print(f"Enjoy your {user_request}.")
                else:
                    print(f"Sorry that's not enough money. Money refunded.")


start_machine()
