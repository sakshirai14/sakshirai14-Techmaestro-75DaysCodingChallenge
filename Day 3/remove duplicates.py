class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in set(nums):
            while nums.count(i)>1:
                nums.remove(i)
        return len(nums)        
