class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}

        # count frequency
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        maxFreq = 0
        total = 0

        # iterate through frequencies
        for count in freq.values():
            if count > maxFreq:
                maxFreq = count
                total = count
            elif count == maxFreq:
                total += count

        return total
