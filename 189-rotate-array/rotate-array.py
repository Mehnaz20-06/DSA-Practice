class Solution(object):
    def rotate(self, nums, k):
        n = len(nums) # 7
        r = k%n # 3
        res = []
        for i in range(n-r,n):
            res.append(nums[i])
        for i in range(0,n-r):
            res.append(nums[i])
        for i in range(0,n):
            nums[i] = res[i]



        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        