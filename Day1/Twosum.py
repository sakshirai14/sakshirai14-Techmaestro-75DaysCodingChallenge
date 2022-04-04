class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l1.append(i)
                    l1.append(j)
                else:
                    continue
        return l1         
