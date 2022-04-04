class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        n=len(nums)
        while(j<n):
            if(nums[j]==0):
                j+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
        return nums    
