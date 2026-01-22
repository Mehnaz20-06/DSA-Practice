class Solution(object):
    def moveZeroes(self, nums):
      k = 0
      for i in range(0,len(nums)):
        if nums[i] == 0:
            continue
        
        nums[k] , nums[i] = nums[i],nums[k]
        k += 1
        


         

                


      
            
        