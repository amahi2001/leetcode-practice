class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0

        # l,r...(len(prices))
        l = 0
        for r in range(1, len(prices)):

            if prices[r] == prices[r-1]:
                continue

            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
        
        return maxP