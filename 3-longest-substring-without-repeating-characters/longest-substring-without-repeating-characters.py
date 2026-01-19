class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        maxlen = 0
        hashmap = {}
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left,hashmap[s[right]] + 1)
            hashmap[s[right]] = right
            length = right - left + 1
            maxlen = max(length,maxlen)
        return maxlen
       