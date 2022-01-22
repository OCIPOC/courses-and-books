from itertools import count


def coin_change(coins: list, amount: int, cache: dict) -> list:
    if amount == 0:
        return []
    elif amount < 0:
        return [-1]
    else:
        res = []
        for coin in coins:
            if (amount, coin) in cache:
                change = cache[(amount, coin)]
            else:
                change = [coin] + coin_change(coins, amount - coin, cache)
                cache[(amount, coin)] = change

            if len(res) == 0 or len(res) > len(change):
                    res = change
        
        return res

print(coin_change([2], 3, {}))
print(coin_change([1, 5], 10, {}))