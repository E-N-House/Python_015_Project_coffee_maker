COINS = {
    "quarter": .25,
    "dime": .1,
    "nickle": .05,
    "penny": .01,
}


def process_money():
    """prompts user to input the amount of coins they are inserting
    Calculates the final value of payment and returns payment
    NOTE has global COINS
    NOTE contains error handling for non number entries"""
    global COINS
    money = 0
    for coin in COINS:
        try:
            money += int(input(f"How many {coin}s do you want to insert?   "))*COINS[coin]
            print(f"You have inserted ${money} so far.")
        except ValueError:
            print(f"You have inserted ${money} so far.")
    return money

