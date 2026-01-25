class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i in range(0,len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False
      
        
        
       
        
        
        
       
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        