class Solution(object):
    def sortColors(self, arr):
        low = 0
        mid = 0
        n = len(arr)
        high = n - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[mid],arr[low] = arr[low],arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1
        



        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        