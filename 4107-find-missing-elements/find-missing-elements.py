class Solution(object):
    def findMissingElements(self, nums):
        nums_set = set(nums)
        low = min(nums)
        high = max(nums)
        missing = []
        for i in range(low+1,high):
            if i not in nums_set:
                missing.append(i)
        return missing

       
            

        
                


       