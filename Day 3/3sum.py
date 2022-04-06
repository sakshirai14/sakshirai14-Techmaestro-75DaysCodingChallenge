class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target=[]
        nums=sorted(nums)
        for x in range(len(nums)-1):
            i=x
            j=len(nums)-1
            curr=nums[x]+nums[i]+nums[j]
            while(i<j):
                curr=nums[x]+nums[i]+nums[j]
                if(curr<0):
                    i+=1
                elif(curr>0):
                    j-=1
                else:
                    if x!=i and x!=j and i!=j:
                        if[nums[x],nums[i],nums[j]] not in target:
                            target.append([nums[x],nums[i],nums[j]])
                    i+=1    
        return target           
        
        
        
