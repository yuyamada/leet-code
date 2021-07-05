# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def solve(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit


prices = [int(s) for s in input().strip().split()]
ans = solve(prices)
print(ans)
