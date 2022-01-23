def coin_change(coins: list, amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c]) 
            print(a, c, dp)
    
    return dp[amount] if dp[amount] != amount + 1 else -1


def coin_change2(coins: list, amount: int, cache = {}) -> int:
    if amount == 0:
        return 0
    elif amount < 0:
        return -1
    elif amount in cache:
        return cache[amount]
    else:
        results = []
        for c in coins:
            res = coin_change2(coins, amount - c, cache)
            if res != -1:
                results.append(1 + res)
        min_change = min(results)
        cache[amount] = min_change
        return min_change
        
print(coin_change([1,2,5], 11))
print(coin_change2([1,2,5], 11))