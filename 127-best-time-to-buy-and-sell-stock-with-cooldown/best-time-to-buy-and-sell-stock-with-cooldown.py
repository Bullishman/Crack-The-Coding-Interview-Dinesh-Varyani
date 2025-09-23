class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev, sell, hold = 0, 0, -float('inf')

        for price in prices:
            temp = sell
            sell = max(sell, hold + price)
            hold = max(hold, prev - price)
            prev = temp

        return sell