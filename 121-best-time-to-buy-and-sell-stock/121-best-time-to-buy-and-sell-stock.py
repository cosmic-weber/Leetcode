class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_:
                min_ = prices[i]
            else:
                profit = max(profit, prices[i]-min_)
                
        return profit