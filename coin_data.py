COINS = {
    "quarter": .25,
    "dime": .1,
    "nickle": .05,
    "penny": .01,
}


def process_money():
    global COINS
    money = 0
    for coin in COINS:
        try:
            money += int(input(f"How many {coin}s do you want to insert?   "))*COINS[coin]
            print(f"You have inserted ${money} so far.")
        except ValueError:
            print(f"You have inserted ${money} so far.")
    return money

