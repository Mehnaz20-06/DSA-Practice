class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        n = len(nums)
        for i in range(0,n):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            seen[nums[i]] = i
        return False

        
       
        
        
        
       
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        