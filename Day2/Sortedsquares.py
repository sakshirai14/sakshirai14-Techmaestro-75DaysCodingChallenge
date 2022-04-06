class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            t=nums[i]*nums[i]
            l.append(t)
        l.sort()
        return l
