class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0

        for price in prices:
            if price < low:
                low = price

            profit = price - low

            if profit > max_profit:
                max_profit = profit

        return max_profit
    

        