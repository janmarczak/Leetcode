class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = 10000000
        max_profit = 0

        for sell in prices:
            if sell <= lowest_price:
                lowest_price = sell
            else:
                # max(max_profit, sell - lowest_price)
                if sell - lowest_price > max_profit:
                    max_profit = sell - lowest_price

        return max_profit
        