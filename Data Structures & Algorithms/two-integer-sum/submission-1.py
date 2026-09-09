class Solution:
    def twoSum(self,nums,target):
        seen={}
        for i,num in enumerate(nums):
            needed=target-nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i
        
