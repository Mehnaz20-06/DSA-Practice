class Solution(object):
    def moveZeroes(self, nums):
        k = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k,n):
            nums[i] = 0

        return nums
     

         

                


      
            
        