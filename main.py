from machine_data import resources


def start_machine():
    is_on = True
    while is_on:
        # Ask the user what they want to do and change it to lowercase
        user_request = input("“What would you like? (espresso/latte/cappuccino):  ").lower()
        # print a report of what it has in stock
        if user_request == "report":
            # TODO format the resources for printing
            print(resources)
            return
        # Turn off the Coffee Machine by entering “off” to the prompt.
        elif user_request == "off":
            is_on = False
            return


start_machine()
# TODO 2. when user orders need to check it has enough to make drink before taking money
# TODO 3 takes penny nickle dime quarter
# TODO 2.1 if yes ask for payment and then return change at end
# TODO 2.2 if not enough money refund
# TODO 3. make the drink and update the resources
