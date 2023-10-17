class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = 10000000
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] <= lowest_price:
                lowest_price = prices[i]
            else:
                if prices[i] - lowest_price > max_profit:
                    max_profit = prices[i] - lowest_price


        return max_profit
        