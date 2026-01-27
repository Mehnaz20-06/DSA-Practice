class Solution(object):
    def findMissingElements(self, nums):
        nums_set = set(nums)
        low = min(nums)
        high = max(nums)
        res = []
        for i in range(low,high+1):
            if i not in nums:
                res.append(i)
        return res
        
                


       