class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        #Mehnaz
        hashmap = {}
        for i , num in enumerate(nums):
            if num in hashmap:
                prevInd = hashmap[num]
                if abs(i - prevInd) <= k:
                    return True
            hashmap[num]= i
        return False
       
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        