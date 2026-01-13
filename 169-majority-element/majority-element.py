class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        m = n // 2
        freq = {}
        for x in nums:
            freq[x] = freq.get(x , 0) + 1
            if freq[x] > m:
                return x
            
        
      
        
    
        