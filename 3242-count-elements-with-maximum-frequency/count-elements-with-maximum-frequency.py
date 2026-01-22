class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x , 0) + 1
        count = 0
        maxim = 0
        for value in freq.values():
            if value > maxim:
                maxim = value
        for value in freq.values():
            if value == maxim:
                count += value
        return count




        