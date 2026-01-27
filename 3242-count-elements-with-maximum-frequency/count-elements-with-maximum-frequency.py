class Solution(object):
    def maxFrequencyElements(self, nums):
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x , 0) + 1
        maxValue = 0
        for value in hashmap.values():
            if value > maxValue:
                maxValue = value
        total = 0
        for value in hashmap.values():
            if value == maxValue:
                total += value
        return total


        