class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 101 # Sets baseline lowest price absurdly high 
        for price in prices:
            profit = max(profit, price - low) # Checks current profit against current day's price - lowest seen price
            if price < low: # Updates lowest seen price when possible
                low = price

        return profit