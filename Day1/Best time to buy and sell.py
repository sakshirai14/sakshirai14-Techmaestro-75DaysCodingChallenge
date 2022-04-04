class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        tmp=0
        for i in range(1,len(prices)):
            if prices[i]-m>tmp:
                tmp=prices[i]-m
            if prices[i]<m:
                m=prices[i]
        return tmp
        
