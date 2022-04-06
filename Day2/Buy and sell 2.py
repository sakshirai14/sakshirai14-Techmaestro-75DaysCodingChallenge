class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,price=0,prices[0]
        for i in range(1,len(prices)):
            if prices[i]<price:
                price=prices[i]
            elif prices[i]>price:
                profit+=prices[i]-price
                price=prices[i]
        return profit
        
