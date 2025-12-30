class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                self.swap(nums,i,j)
                j += 1
        
    def swap(self ,nums,i,j):
        nums[i] , nums[j] = nums[j] , nums[i]
            
        