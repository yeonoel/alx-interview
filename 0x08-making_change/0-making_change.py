"""Change comes from within"""

def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total."""
    nb = len(coins)
    dp = [-1] * (total + 1)
    dp[0] = 0
    coins = sorted(coins)
    for i in range(1, nb + 1):
        for j in range(coins[i - 1], total + 1):
            if j == coins[i - 1]:
                dp[j] = 1
            elif dp[j - coins[i - 1]] != -1:
                if dp[j] == -1:
                    dp[j] = dp[j - coins[i - 1]] + 1
                else:
                    dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
    return dp[total]
