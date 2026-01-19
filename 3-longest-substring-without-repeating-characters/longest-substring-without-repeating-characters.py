class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        left = 0
        maxLen = 0
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left,hashmap[s[right]] + 1)
            hashmap[s[right]] = right
            length = right - left + 1
            maxLen = max(length,maxLen)
        return maxLen
       